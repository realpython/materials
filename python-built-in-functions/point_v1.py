# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


class Point:
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = self.validate(x)

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = self.validate(y)

    def validate(self, value):
        if not isinstance(value, int | float):
            raise ValueError("coordinates must be numbers")
        return value
