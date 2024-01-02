class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
        return False

    def __add__(self, other):
        return type(self)(self.items + other.items)

    def __iadd__(self, other):
        self.items.extend(other.items)
        return self

    def __iter__(self):
        return iter(self.items[::-1])

    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __reversed__(self):
        return type(self)(reversed(self.items))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.items == other.items

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.items < other.items

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.items > other.items

    def __le__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.items <= other.items

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"'other' must be of type '{type(self).__name__}'")
        return self.items >= other.items
