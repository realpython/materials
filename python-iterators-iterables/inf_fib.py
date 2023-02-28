class FibonacciInfIterator:
    def __init__(self):
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        fib_number = self._current
        self._current, self._next = self._next, self._current + self._next
        return fib_number
