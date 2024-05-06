class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        if self.x == self.y == 0:
            return False
        return True


origin = Point(0, 0)
print(bool(origin))
point = Point(2, 4)
print(bool(point))
