from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * radius**2  # noqa: F821


if __name__ == "__main__":
    Circle(5).area()
