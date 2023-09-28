from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * pi * radius**2


if __name__ == "__main__":
    Circle(5).area()
