class SquareIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration
        square = self.values[self.index] ** 2
        self.index += 1
        return square
