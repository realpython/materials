from collections import namedtuple
from typing import NamedTuple

from pympler import asizeof

PointNamedTuple = namedtuple("PointNamedTuple", "x y z")


class PointTypedNamedTuple(NamedTuple):
    x: int
    y: int
    z: int


namedtuple_memory = asizeof.asizeof(PointNamedTuple(x=1, y=2, z=3))
typed_namedtuple_memory = asizeof.asizeof(PointTypedNamedTuple(x=1, y=2, z=3))

print(f"namedtuple:        {namedtuple_memory} bytes")
print(f"typing.NamedTuple: {typed_namedtuple_memory} bytes")
