class Factorial:
    def __init__(self, number):
        self._number = number
        self._cache = {0: 1, 1: 1}
        self._factorial = self._calculate_factorial(number)
        del self._cache

    def _calculate_factorial(self, number):
        if number in self._cache:
            return self._cache[number]
        current_factorial = number * self._calculate_factorial(number - 1)
        self._cache[number] = current_factorial
        return current_factorial

    @property
    def number(self):
        return self._number

    @property
    def factorial(self):
        return self._factorial

    def __str__(self) -> str:
        return f"{self._number}! = {self._factorial}"

    def __repr__(self):
        return f"{type(self).__name__}({self._number})"
