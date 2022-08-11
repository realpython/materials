from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable):
        self.data = [self._validate_number(item) for item in iterable]

    def __setitem__(self, index, item):
        self.data[index] = self._validate_number(item)

    def insert(self, index, item):
        self.data.insert(index, self._validate_number(item))

    def append(self, item):
        self.data.append(self._validate_number(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self._validate_number(item) for item in other)

    def _validate_number(self, value):
        if isinstance(value, (int, float, complex)):
            return value
        raise TypeError(f"numeric value expected, got {type(value).__name__}")
