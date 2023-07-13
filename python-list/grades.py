class GradeList(list):
    def __init__(self, grades):
        grades = [self._validate(grade) for grade in grades]
        super().__init__(grades)

    def __setitem__(self, index, grade):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            grades = [self._validate(grade) for grade in grade]
            return super().__setitem__(slice(start, stop, step), grades)
        super().__setitem__(index, self._validate(grade))

    def __add__(self, grades):
        grades = [self._validate(grade) for grade in grades]
        grades = super().__add__(grades)
        return self.__class__(grades)

    __radd__ = __add__

    def __iadd__(self, grades):
        grades = [self._validate(grade) for grade in grades]
        return super().__iadd__(grades)

    def append(self, grade):
        return super().append(self._validate(grade))

    def extend(self, grades):
        grades = [self._validate(grade) for grade in grades]
        return super().extend(grades)

    def average(self):
        return sum(self) / len(self)

    def _validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("grades must be numeric")
        if not (0 <= value <= 100):
            raise ValueError("grade must be between 0 and 100")
        return value
