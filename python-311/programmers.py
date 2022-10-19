import json
import pathlib
from dataclasses import dataclass
from typing import Any, Self, TypeAlias

Info: TypeAlias = dict[str, Any]

programmers = json.loads(
    pathlib.Path("programmers.json").read_text(encoding="utf-8")
)


@dataclass
class Person:
    name: str
    life_span: tuple[int, int]

    @classmethod
    def from_dict(cls, info: Info) -> Self:
        return cls(
            name=f"{info['name']['first']} {info['name']['last']}",
            life_span=(info["birth"]["year"], info["death"]["year"]),
        )


def convert_pair(first: Info, second: Info) -> tuple[Person, Person]:
    return Person.from_dict(first), Person.from_dict(second)
