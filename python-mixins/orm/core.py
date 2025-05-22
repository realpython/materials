import atexit
import inspect
import os
import re
import sqlite3
import textwrap
import typing
from dataclasses import MISSING, Field, dataclass, field, fields
from functools import cached_property
from typing import Any, ClassVar, Iterator, Type, TypeVar

DATABASE_FILE = os.getenv("DATABASE", ":memory:")
PRIMARY_KEY_COLUMN = "pk"
SQL_COLUMN_TYPES = {
    bool: "NUMERIC",
    bytes: "BLOB",
    float: "REAL",
    int: "INTEGER",
    str: "TEXT",
}

_T = TypeVar("_T", bound="ActiveRecord")


class DataClassMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        cls = super().__new__(mcs, name, bases, attrs)
        return dataclass(**kwargs)(cls)


class ActiveRecordMeta(DataClassMeta):
    connection = sqlite3.connect(DATABASE_FILE)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    connection.autocommit = True
    atexit.register(connection.close)

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if len(bases) > 0:
            cls.__table__ = SQLTable(cls)
            cls.__table__.create()
        return cls


class ActiveRecord(metaclass=ActiveRecordMeta):
    __table__: ClassVar["SQLTable"]
    pk: int | None = field(kw_only=True, default=None)

    @classmethod
    def find_all(cls: type[_T]) -> Iterator[_T]:
        return recursive_fetch(cls, cls.__table__.select_all())

    @classmethod
    def find_by(cls: type[_T], **parameters) -> Iterator[_T]:
        if not parameters:
            raise ValueError("missing query conditions")
        return recursive_fetch(cls, cls.__table__.select_where(**parameters))

    @classmethod
    def find(cls: type[_T], *, pk: int) -> _T:
        try:
            return next(cls.find_by(pk=pk))
        except StopIteration as ex:
            raise ValueError(f"{cls.__name__} with pk={pk} not found") from ex

    def save(self) -> None:
        if self.pk is None:
            cursor = self.__table__.insert(self)
            self.pk = cursor.lastrowid
        else:
            self.__table__.update(self)

    def delete(self) -> None:
        self.__table__.delete(self)
        self.pk = None

    def __setattr__(self, name: str, value: Any) -> None:
        if name == PRIMARY_KEY_COLUMN:
            if frame := inspect.currentframe():
                if calling_frame := frame.f_back:
                    local_self = calling_frame.f_locals.get("self", None)
                    if local_self is not self:
                        raise AttributeError(
                            "primary key is managed by the database"
                        )
        super().__setattr__(name, value)


class SQLTable:
    def __init__(self, cls: type[_T]) -> None:
        self.cls = cls
        self.sql = SQLQueryGenerator(self)

    @cached_property
    def name(self) -> str:
        return f"{snake_case(self.cls.__name__).rstrip("s")}s"

    @cached_property
    def columns(self) -> list["SQLColumn"]:
        return [
            SQLColumn(class_field)
            for class_field in fields(self.cls)
            if class_field.name != PRIMARY_KEY_COLUMN
        ]

    @cached_property
    def foreign_keys(self) -> dict[str, type[_T]]:
        return {
            column.name: column.foreign_table.cls
            for column in self.columns
            if column.foreign_table
        }

    def create(self) -> sqlite3.Cursor:
        return self.cls.connection.execute(self.sql.create.statement)

    def insert(self, record: _T) -> sqlite3.Cursor:
        if record.pk is not None:
            raise ValueError("record has a primary key")
        query = self.sql.insert(record)
        return self.cls.connection.execute(query.statement, query.values)

    def update(self, record: _T) -> sqlite3.Cursor:
        if record.pk is None:
            raise ValueError("record has no primary key")
        query = self.sql.update(record)
        return self.cls.connection.execute(query.statement, query.values)

    def delete(self, record: _T) -> sqlite3.Cursor:
        if record.pk is None:
            raise ValueError("record hasn't been saved to database")
        query = self.sql.delete(record)
        return self.cls.connection.execute(query.statement, query.values)

    def select_all(self) -> sqlite3.Cursor:
        return self.cls.connection.execute(self.sql.select_all.statement)

    def select_where(self, **parameters) -> sqlite3.Cursor:
        query = self.sql.select_where(**parameters)
        return self.cls.connection.execute(query.statement, query.values)


class SQLColumn:
    name: str
    type: str
    default: Any
    foreign_table: SQLTable | None

    def __init__(self, class_field: Field) -> None:
        field_type = primary_type(class_field.type)
        if issubclass(field_type, ActiveRecord):
            self.name = f"{class_field.name}_{PRIMARY_KEY_COLUMN}"
            self.type = SQL_COLUMN_TYPES.get(int, "TEXT")
            self.foreign_table = SQLTable(field_type)
        else:
            self.name = class_field.name
            self.type = SQL_COLUMN_TYPES.get(field_type, "TEXT")
            self.foreign_table = None
        if class_field.default_factory is not MISSING:
            self.default = class_field.default_factory()
        elif class_field.default is not MISSING:
            self.default = class_field.default
        else:
            self.default = MISSING

    @cached_property
    def definition(self) -> str:
        sql = f"{self.name} {self.type}"
        if self.foreign_table:
            sql += (
                " REFERENCES "
                f"{self.foreign_table.name}({PRIMARY_KEY_COLUMN})"
            )
        if self.default is MISSING:
            sql += " NOT NULL"
        elif self.default is not None:
            sql += f" DEFAULT {self.default!r}"
        return sql


class SQLQuery:
    def __init__(
        self, statement: str, parameters: dict[str, Any] | None = None
    ) -> None:
        self.statement = statement
        self.parameters = parameters or {}
        self.values = rename(self.parameters)

    def __str__(self) -> str:
        result = self.statement
        for key, value in self.values.items():
            if value is None:
                result = result.replace(f"=:{key}", " IS NULL")
            else:
                result = result.replace(f":{key}", repr(value))
        return result + ";"


class SQLQueryGenerator:
    def __init__(self, table: "SQLTable") -> None:
        self.table = table

    @cached_property
    def create(self) -> SQLQuery:
        column_definitions = [
            f"{PRIMARY_KEY_COLUMN} INTEGER PRIMARY KEY AUTOINCREMENT",
            *(column.definition for column in self.table.columns),
        ]
        return SQLQuery(
            textwrap.dedent(
                f"""\
                CREATE TABLE IF NOT EXISTS {self.table.name}(
                    {",\n                    ".join(column_definitions)}
                )"""
            )
        )

    def insert(self, record: _T) -> SQLQuery:
        column_names = ", ".join(column.name for column in self.table.columns)
        placeholders = ", ".join(
            f":{column.name}" for column in self.table.columns
        )
        return SQLQuery(
            (
                f"INSERT INTO {self.table.name}({column_names}) "
                f"VALUES ({placeholders})"
            ),
            dict(vars(record)),
        )

    def update(self, record: _T) -> SQLQuery:
        placeholders = ", ".join(
            f"{column.name}=:{column.name}" for column in self.table.columns
        )
        return SQLQuery(
            (
                f"UPDATE {self.table.name} "
                f"SET {placeholders} "
                f"WHERE {PRIMARY_KEY_COLUMN}=:{PRIMARY_KEY_COLUMN}"
            ),
            dict(vars(record)),
        )

    def delete(self, record: _T) -> SQLQuery:
        return SQLQuery(
            (
                f"DELETE FROM {self.table.name} "
                f"WHERE {PRIMARY_KEY_COLUMN}=:{PRIMARY_KEY_COLUMN}"
            ),
            dict(vars(record)),
        )

    @cached_property
    def select_all(self) -> SQLQuery:
        return SQLQuery(f"SELECT * FROM {self.table.name}")

    def select_where(self, **parameters) -> SQLQuery:
        values = rename(parameters)
        conditions = " AND ".join(f"{param}=:{param}" for param in values)
        return SQLQuery(
            f"SELECT * FROM {self.table.name} WHERE {conditions}",
            values,
        )


def recursive_fetch(cls: type[_T], cursor: sqlite3.Cursor) -> Iterator[_T]:
    for row in cursor.fetchall():
        attrs = {}
        for column_name in row.keys():
            if fk := cls.__table__.foreign_keys.get(column_name):
                name = column_name.removesuffix(f"_{PRIMARY_KEY_COLUMN}")
                attrs[name] = fk.find(pk=row[column_name])
            else:
                attrs[column_name] = row[column_name]
        yield cls(**attrs)


def rename(parameters: dict[str, Any]) -> dict[str, Any]:
    values = {}
    for key, value in parameters.items():
        if isinstance(value, ActiveRecord):
            values[f"{key}_{PRIMARY_KEY_COLUMN}"] = value.pk
        else:
            values[key] = value
    return values


def primary_type(type_hint: Type) -> type:
    if args := typing.get_args(type_hint):
        match [arg for arg in args if arg is not type(None)]:
            case [x] if x is not None:
                return x
            case []:
                raise TypeError("no primary types found")
            case _:
                raise TypeError("cannot have multiple primary types")

    if type_hint is None:
        raise TypeError("type cannot be None")

    return type_hint


def snake_case(text: str) -> str:
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", text).lower()
