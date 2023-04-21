class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
        self.width = value
        self.height = value
