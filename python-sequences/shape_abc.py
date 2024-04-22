from collections.abc import MutableSequence


class ShapePoints(MutableSequence):
    MIN_POINTS = 3

    def __init__(self, points):
        self.points = list(points)
        if len(self.points) < self.MIN_POINTS:
            raise ValueError(
                f"Shape must have at least {self.MIN_POINTS} points"
            )
        if self.points[0] != self.points[-1]:
            self.points.append(self.points[0])

    def __repr__(self):
        return f"ShapePoints({self.points})"

    def __getitem__(self, index):
        return self.points[index]

    def __len__(self):
        return len(self.points) - 1

    def __iter__(self):
        return iter(self.points)

    def __contains__(self, item):
        print("Checking if item is in ShapePoints")
        return item in self.points

    def __delitem__(self, index):
        if len(self) < self.MIN_POINTS + 1:
            raise ValueError(
                f"Shape must have at least {self.MIN_POINTS} points"
            )
        if index in (0, len(self.points) - 1, -1):
            del self.points[0]
            self.points[-1] = self.points[0]
        else:
            del self.points[index]

    def __setitem__(self, index, value):
        if index in (0, len(self.points) - 1, -1):
            self.points[0] = value
            self.points[-1] = value
        else:
            self.points[index] = value

    def insert(self, index, value):
        if index in (0, len(self.points) - 1, -1):
            self.points.insert(0, value)
            self.points[-1] = value
        else:
            self.points.insert(index, value)

    def count(self, value):
        return self.points[:-1].count(value)

    def append(self, value):
        self.points.append(self.points[0])
        self.points[-2] = value
