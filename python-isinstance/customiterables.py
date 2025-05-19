from collections.abc import Iterable


class CustomIterableOne(Iterable):

    def __init__(self, last_value):
        self.last_value = last_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.last_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration()


class CustomIterableTwo:

    def __init__(self, last_value):
        self.last_value = last_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.last_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration()


class CustomIterableThree:

    def __init__(self, last_value):
        self.last_value = last_value

    def __getitem__(self, index):
        if index >= self.last_value:
            raise IndexError
        return index + 1
