class ReusableRange:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            stop, start = start, 0
        self._range = range(start, stop, step)
        self._iter = iter(self._range)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            self._iter = iter(self._range)
            raise
