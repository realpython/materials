import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if (not isinstance(value, int | float)) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

    def area(self):
        return math.pi * self._radius**2
