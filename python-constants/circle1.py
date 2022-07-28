# circle1.py


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def projected_volume(self):
        return 4 / 3 * 3.14 * self.radius**3

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"
