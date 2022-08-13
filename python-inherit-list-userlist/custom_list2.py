from collections import UserList


class CustomList(UserList):
    def join(self, separator=" "):
        return separator.join(str(item) for item in self)

    def map(self, action):
        return type(self)(action(item) for item in self.data)

    def filter(self, predicate):
        return type(self)(item for item in self if predicate(item))

    def for_each(self, func):
        for item in self.data:
            func(item)
