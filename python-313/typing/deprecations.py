"""Demonstration of PEP 702: Marking deprecations using the type system

The deprecations should be marked in PyCharm and VS Code.

Use PyLance in VS Code by setting Python › Analysis: Type Checking Mode or run
the Pyright CLI:

    $ python -m pip install pyright
    $ pyright --pythonversion 3.13 .

Note that showing warnings with Pyright requires setting the reportDeprecated
option. This is done in the accompanying pyproject.toml.
"""

from typing import overload
from warnings import deprecated


@deprecated("Use + instead of calling concatenate()")
def concatenate(first: str, second: str) -> str:
    return first + second


@overload
@deprecated("add() is only supported for floats")
def add(x: int, y: int) -> int: ...
@overload
def add(x: float, y: float) -> float: ...


def add(x, y):
    return x + y


class Version:
    def __init__(self, major: int, minor: int = 0, patch: int = 0) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    @property
    @deprecated("Use .patch instead")
    def bugfix(self):
        return self.patch

    def bump(self, part: str) -> None:
        if part == "major":
            self.major += 1
            self.minor = 0
            self.patch = 0
        elif part == "minor":
            self.minor += 1
            self.patch = 0
        elif part == "patch":
            self.patch += 1
        else:
            raise ValueError("part must be 'major', 'minor', or 'patch'")

    @deprecated("Use .bump() instead")
    def increase(self, part: str) -> None:
        return self.bump(part)

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


@deprecated("Use Version instead")
class VersionType:
    def __init__(self, major: int, minor: int = 0, patch: int = 0) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch


concatenate("three", "thirteen")
add(3, 13)
VersionType(3, 13)

version = Version(3, 13)
version.increase("patch")
print(version)
print(version.bugfix)
