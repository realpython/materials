from math import pi
from typing import Protocol, runtime_checkable


@runtime_checkable
class Shape(Protocol):
    def get_area(self) -> float: ...

    def get_perimeter(self) -> float: ...


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius**2

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius


class Square:
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
