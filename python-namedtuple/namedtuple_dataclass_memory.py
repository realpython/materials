from collections import namedtuple
from dataclasses import dataclass

from pympler import asizeof

PointNamedTuple = namedtuple("PointNamedTuple", "x y z")


@dataclass
class PointDataClass:
    x: int
    y: int
    z: int


namedtuple_memory = asizeof.asizeof(PointNamedTuple(x=1, y=2, z=3))
dataclass_memory = asizeof.asizeof(PointDataClass(x=1, y=2, z=3))
gain = 100 - namedtuple_memory / dataclass_memory * 100

print(f"namedtuple: {namedtuple_memory} bytes ({gain:.2f}% smaller)")
print(f"data class: {dataclass_memory} bytes")
