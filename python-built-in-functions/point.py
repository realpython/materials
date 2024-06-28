import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_polar(cls, distance, angle):
        return cls(
            x=distance * math.cos(math.radians(angle)),
            y=distance * math.sin(math.radians(angle)),
        )
