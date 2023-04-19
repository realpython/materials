from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

    def get_perimeter(self):
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return 4 * self.side
