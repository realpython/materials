# from __future__ import annotations

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from people.club import Club

from people.club import Club


class Person:
    def __init__(self, name, age, clubs: list[Club] = []):
        self.name = name
        self.age = age
        self.clubs = clubs

    def __str__(self):
        return f"{self.name} ({self.age})"
