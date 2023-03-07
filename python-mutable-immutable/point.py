# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

#     @property
#     def x(self):
#         return self._x

#     @property
#     def y(self):
#         return self._y

#     def __repr__(self):
#         return f"{type(self).__name__}(x={self.x}, y={self.y})"


class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[f"_{self._name}"]

    def __set__(self, instance, value):
        raise AttributeError(f"can't set attribute {self._name}")


class Point:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
