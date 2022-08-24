class NumberList(list):
    def __init__(self, iterable):
        super().__init__(self._validate_number(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, self._validate_number(item))

    def insert(self, index, item):
        super().insert(index, self._validate_number(item))

    def append(self, item):
        super().append(self._validate_number(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(self._validate_number(item) for item in other)

    def _validate_number(self, value):
        if isinstance(value, (int, float, complex)):
            return value
        raise TypeError(f"numeric value expected, got {type(value).__name__}")
