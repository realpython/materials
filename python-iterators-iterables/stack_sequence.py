class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)
