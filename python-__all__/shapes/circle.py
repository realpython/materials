from math import pi as _pi

from shapes.utils import validate


class Circle:
    def __init__(self, radius):
        self.radius = validate(radius)

    def area(self):
        return _pi * self.radius**2
