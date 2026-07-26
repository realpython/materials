from abc import ABC, abstractmethod


class IterMixin:
    # __iter__ works IF the class inheriting the mixin
    # already provides __getitem__ and __len__.
    def __iter__(self):
        print("Hey from inside IterMixin.__iter__.")
        index = 0
        while index < len(self):
            yield self[index]
            index += 1


class Sequence(IterMixin, ABC):
    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __len__(self):
        pass


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
