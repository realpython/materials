import math


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value


class Circle:
    radius = PositiveNumber()

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)


class Square:
    side = PositiveNumber()

    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)


class Rectangle:
    height = PositiveNumber()
    width = PositiveNumber()

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
