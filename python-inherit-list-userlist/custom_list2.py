from collections import UserList


class CustomList(UserList):
    def join(self, sep=" "):
        return sep.join(self.data)

    def map(self, action):
        return type(self)(action(item) for item in self.data)

    def filter(self, predicate):
        return type(self)(item for item in self if predicate(item))

    def for_each(self, func):
        for item in self.data:
            yield func(item)
