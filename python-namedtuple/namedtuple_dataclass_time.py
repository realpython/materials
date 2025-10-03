from collections import namedtuple
from dataclasses import dataclass
from time import perf_counter


def average_time(structure, test_func):
    time_measurements = []
    for _ in range(1_000_000):
        start = perf_counter()
        test_func(structure)
        end = perf_counter()
        time_measurements.append(end - start)
    return sum(time_measurements) / len(time_measurements) * int(1e9)


def time_structure(structure):
    structure.x
    structure.y
    structure.z


PointNamedTuple = namedtuple("PointNamedTuple", "x y z", defaults=[3])


@dataclass
class PointDataClass:
    x: int
    y: int
    z: int


namedtuple_time = average_time(PointNamedTuple(x=1, y=2, z=3), time_structure)
dataclass_time = average_time(PointDataClass(x=1, y=2, z=3), time_structure)

print(f"namedtuple: {namedtuple_time:.2f} ns")
print(f"data class: {dataclass_time:.2f} ns")
