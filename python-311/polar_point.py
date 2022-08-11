import math
from dataclasses import dataclass
from typing import Self


@dataclass
class PolarPoint:
    r: float
    φ: float

    @classmethod
    def from_xy(cls, x: float, y: float) -> Self:
        return cls(r=math.hypot(x, y), φ=math.atan2(y, x))


print(PolarPoint.from_xy(3, 4))
