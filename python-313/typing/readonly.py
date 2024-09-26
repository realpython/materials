"""Demonstration of PEP 705: TypedDict: read-only items

Use PyLance in VS Code by setting Python › Analysis: Type Checking Mode or run
the Pyright CLI:

    $ python -m pip install pyright $ pyright --pythonversion 3.13 .

Extension of TypedDict:
https://realpython.com/python38-new-features/#more-precise-types
"""

from typing import NotRequired, ReadOnly, TypedDict

# class Version(TypedDict):
#     version: str
#     release_year: NotRequired[int | None]


# class PythonVersion(TypedDict):
#     version: str
#     release_year: int


class Version(TypedDict):
    version: ReadOnly[str]
    release_year: ReadOnly[NotRequired[int | None]]


class PythonVersion(TypedDict):
    version: ReadOnly[str]
    release_year: ReadOnly[int]


py313 = PythonVersion(version="3.13", release_year=2024)

# Alternative syntax, using TypedDict as an annotation
# py313: PythonVersion = {"version": "3.13", "release_year": 2024}


def get_version_info(ver: Version) -> str:
    if "release_year" in ver:
        return f"Version {ver['version']} released in {ver['release_year']}"
    else:
        return f"Version {ver['version']}"


# Only allowed to use PythonVersion instead of Version if the fields are ReadOnly
print(get_version_info(py313))
