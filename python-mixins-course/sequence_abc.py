from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def __iter__(self):
        index = 0
        while index < len(self):
            yield self[index]
            index += 1


class MyRange(Sequence):
    def __init__(self, stop):
        self.stop = stop  # Assume that `stop` is >= 0.

    def __getitem__(self, index):
        if 0 <= index < self.stop:
            return index
        raise IndexError

    def __len__(self):
        return self.stop


r = MyRange(10)
for number in r:
    print(number)