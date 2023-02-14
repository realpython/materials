import math
from collections import namedtuple


class Point(namedtuple("Point", "x y")):
    __slots__ = ()

    def distance(self, other: "Point") -> float:
        return math.dist((self.x, self.y), (other.x, other.y))
