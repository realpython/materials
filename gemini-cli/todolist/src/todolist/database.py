from functools import cached_property

from peewee import (
    BooleanField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
    TextField,
)
from platformdirs import user_cache_path

db_file = user_cache_path() / __package__ / f"{__package__}.db"
db_file.parent.mkdir(parents=True, exist_ok=True)

db = SqliteDatabase(db_file)


class TaskList(Model):
    name = TextField(null=False, unique=True)

    class Meta:
        database = db
        table_name = "lists"


class Task(Model):
    emoji = TextField(null=True)
    name = TextField(null=False)
    done = BooleanField(null=False, default=False)
    task_list = ForeignKeyField(TaskList, backref="tasks", on_delete="CASCADE")

    class Meta:
        database = db
        table_name = "tasks"

    @cached_property
    def pretty_name(self) -> str:
        if self.emoji:
            return f"{self.emoji} {self.name}"
        else:
            return str(self.name)


db.create_tables([TaskList, Task], safe=True)
