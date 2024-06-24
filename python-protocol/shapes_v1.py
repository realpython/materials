from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius**2

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def get_area(self) -> float:
        return self.side**2

    def get_perimeter(self) -> float:
        return 4 * self.side


def print_shape_info(shape: Shape):
    print(f"Area: {shape.get_area()}")
    print(f"Perimeter: {shape.get_perimeter()}")


circle = Circle(10)
square = Square(5)

print_shape_info(circle)
print_shape_info(square)
