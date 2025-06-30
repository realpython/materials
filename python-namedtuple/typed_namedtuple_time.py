from collections import namedtuple
from time import perf_counter
from typing import NamedTuple


def average_time(structure, test_func):
    time_measurements = []
    for _ in range(1_000_000):
        start = perf_counter()
        test_func(structure)
        end = perf_counter()
        time_measurements.append(end - start)
    return sum(time_measurements) / len(time_measurements) * int(1e9)


def time_structure(structure):
    "x" in structure._fields
    "missing_field" in structure._fields
    2 in structure
    "missing_value" in structure
    structure.y


PointNamedTuple = namedtuple("PointNamedTuple", "x y z")


class PointTypedNamedTuple(NamedTuple):
    x: int
    y: int
    z: int


namedtuple_time = average_time(PointNamedTuple(x=1, y=2, z=3), time_structure)
typed_namedtuple_time = average_time(
    PointTypedNamedTuple(x=1, y=2, z=3), time_structure
)

print(f"namedtuple:        {namedtuple_time:.2f} ns")
print(f"typing.NamedTuple: {typed_namedtuple_time:.2f} ns")
