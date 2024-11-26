# from __future__ import annotations

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from people.person import Person

from people.person import Person


class Club:
    def __init__(self, name, members: list[Person] = []):
        self.name = name
        self.members = members

    def __str__(self):
        return f"{self.name} ({len(self.members)} members)"
