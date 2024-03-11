from math import pi as _pi


class Circle:
    def __init__(self, radius):
        self.radius = _validate(radius)

    def area(self):
        return _pi * self.radius**2


class Square:
    def __init__(self, side):
        self.side = _validate(side)

    def area(self):
        return self.side**2


def _validate(value):
    if not isinstance(value, int | float) or value <= 0:
        raise ValueError("positive number expected")
    return value
