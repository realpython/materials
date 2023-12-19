class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.x >= other.x and self.y >= other.y

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.x != other.x and self.y != other.y
