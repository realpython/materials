class Fibonaccier:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._previous = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._stop:
            raise StopIteration
        self._index += 1
        fib_number = self._previous
        self._previous, self._next = self._next, self._previous + self._next
        return fib_number
