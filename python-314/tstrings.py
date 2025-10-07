from dataclasses import dataclass
from string.templatelib import Interpolation, Template, convert
from typing import Any


@dataclass(frozen=True)
class SQLQuery:
    statement: str
    params: list[Any]

    def __init__(self, template: Template) -> None:
        items, params = [], []
        for item in template:
            match item:
                case str():
                    items.append(item)
                case Interpolation(value, _, conversion, format_spec):
                    converted = convert(value, conversion)
                    if format_spec:
                        converted = format(converted, format_spec)
                    params.append(converted)
                    items.append("?")
        super().__setattr__("statement", "".join(items))
        super().__setattr__("params", params)


def find_users_query_v1(name: str) -> str:
    """Return a SQL query to find users by name."""
    return f"SELECT * FROM users WHERE name = '{name}'"


# Uncomment for Python 3.14:
#
# def find_users_query_v2(name: str) -> Template:
#     """Return a SQL query to find users by name."""
#     return t"SELECT * FROM users WHERE name = '{name}'"
#
#
# def find_users(name: str) -> SQLQuery:
#     """Return a SQL query to find users by name."""
#     return SQLQuery(t"SELECT * FROM users WHERE name = {name}")


def render(template: Template) -> str:
    return "".join(
        f"{text}{value}"
        for text, value in zip(template.strings, template.values, strict=False)
    )


def safer_render(template: Template) -> str:
    items = []
    for item in template:
        if isinstance(item, str):
            items.append(item)
        else:
            sanitized = str(item.value).replace("'", "''")
            items.append(sanitized)
    return "".join(items)


if __name__ == "__main__":
    # Insecure f-strings
    print(find_users_query_v1("' OR '1'='1"))

    # Uncomment for Python 3.14:
    #
    # # More secure t-strings
    # print(find_users_query_v2("' OR '1'='1"))
    #
    # # Insecure way of rendering t-strings into plain strings
    # print(render(find_users_query_v2("' OR '1'='1")))
    #
    # # More secure way of rendering t-strings
    # print(safer_render(find_users_query_v2("' OR '1'='1")))
    #
    # # Rendering t-strings into an alternative representation
    # print(find_users("' OR '1'='1"))
