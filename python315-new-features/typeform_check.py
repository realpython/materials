from typing import TypeForm, reveal_type

def parse_old[T](value: str, typ: type[T]) -> T: ...

def parse_new[T](value: str, typ: TypeForm[T]) -> T: ...

reveal_type(parse_old("42", int))
reveal_type(parse_old("42", int | None))
reveal_type(parse_new("42", int | None))
reveal_type(parse_new("42", list[int]))
parse_new("42", 42)
