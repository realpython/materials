# circle3.py

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def projected_volume(self):
        return 4 / 3 * math.pi * self.radius**3

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"
