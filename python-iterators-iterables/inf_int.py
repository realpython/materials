class InfIntegers:
    def __init__(self):
        self._number = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self._number
        self._number += 1
        return number
