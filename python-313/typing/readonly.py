"""Demonstration of PEP 705: TypedDict: read-only items

Use PyLance in VS Code by setting Python › Analysis: Type Checking Mode or run
the Pyright CLI:

    $ python -m pip install pyright $ pyright --pythonversion 3.13 .

Extension of TypedDict:
https://realpython.com/python38-new-features/#more-precise-types
"""

from typing import NotRequired, ReadOnly, TypedDict

# %% Without ReadOnly

# class Version(TypedDict):
#     version: str
#     release_year: NotRequired[int | None]


# class PythonVersion(TypedDict):
#     version: str
#     release_year: int


# %% Using ReadOnly
#
# Can only use PythonVersion as a Version if the differing fields are ReadOnly
class Version(TypedDict):
    version: str
    release_year: ReadOnly[NotRequired[int | None]]

    # Note that ReadOnly can be nested with other special forms in any order
    # release_year: NotRequired[ReadOnly[int | None]]


class PythonVersion(TypedDict):
    version: str
    release_year: ReadOnly[int]


# %% Work with Version and PythonVersion
#
def get_version_info(ver: Version) -> str:
    if "release_year" in ver:
        return f"Version {ver['version']} released in {ver['release_year']}"
    else:
        return f"Version {ver['version']}"


py313 = PythonVersion(version="3.13", release_year=2024)

# Alternative syntax, using TypedDict as an annotation
# py313: PythonVersion = {"version": "3.13", "release_year": 2024}

print(get_version_info(py313))
