class CustomList(list):
    def join(self, sep=" "):
        return sep.join(str(item) for item in self)

    def map(self, action):
        return type(self)(action(item) for item in self)

    def filter(self, predicate):
        return type(self)(item for item in self if predicate(item))

    def for_each(self, func):
        for item in self:
            yield func(item)
