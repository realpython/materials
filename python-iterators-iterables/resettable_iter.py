class ResettableRange:
    def __init__(self, start=0, end=None, step=1, *, resettable=False):
        if end is None:
            end, start = start, 0
        self._start = start
        self._end = end
        self._step = step
        self._resettable = resettable

    def __iter__(self):
        return self

    def __next__(self):
        if self._start >= self._end:
            if self._resettable:
                self._start = 0
            raise StopIteration
        value = self._start
        self._start += self._step
        return value
