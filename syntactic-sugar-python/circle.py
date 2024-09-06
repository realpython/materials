from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius


circle = Circle(10)
print(circle.radius)
print(circle.area())
print(circle.perimeter())
