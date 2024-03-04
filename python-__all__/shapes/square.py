from shapes.utils import validate


class Square:
    def __init__(self, side):
        self.side = validate(side)

    def area(self):
        return self.side**2
