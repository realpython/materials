from typing import NamedTuple

scientists = [
    {
        "name": {"first": "Grace", "last": "Hopper"},
        "birth": {"year": 1906, "month": 12, "day": 9},
        "death": {"year": 1992, "month": 1, "day": 1},
    },
    {"name": {"first": "Euclid"}},
    {"name": {"first": "Abu Nasr", "last": "Al-Farabi"}, "birth": None},
    {
        "name": {"first": "Srinivasa", "last": "Ramanujan"},
        "birth": {"year": 1887},
        "death": {"month": 4, "day": 26},
    },
    {
        "name": {"first": "Ada", "last": "Lovelace"},
        "birth": {"year": 1815},
        "death": {"year": 1852},
    },
    {
        "name": {"first": "Charles", "last": "Babbage"},
        "birth": {"year": 1791, "month": 12, "day": 26},
        "death": {"year": 1871, "month": 10, "day": 18},
    },
]


class Person(NamedTuple):
    name: str
    life_span: tuple


def dict_to_person(info):
    """Convert a dictionary to a Person object"""
    return Person(
        name=f"{info['name']['first']} {info['name']['last']}",
        life_span=(info["birth"]["year"], info["death"]["year"]),
    )


def convert_pair(first, second):
    """Convert two dictionaries to Person objects"""
    return dict_to_person(first), dict_to_person(second)
