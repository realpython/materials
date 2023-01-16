# circle2.py

PI = 3.14


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius**2

    def perimeter(self):
        return 2 * PI * self.radius

    def projected_volume(self):
        return 4 / 3 * PI * self.radius**3

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"
