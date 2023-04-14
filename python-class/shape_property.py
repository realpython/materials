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

    def compute_area(self):
        return round(math.pi * self._radius**2, 2)


class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._side = value

    def compute_area(self):
        return round(self._side**2, 2)
