class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __getitem__(self, index):
        try:
            return self.items[index]
        except IndexError:
            raise IndexError(
                f"Your stack only has {len(self)} items!"
            ) from None

    def __len__(self):
        return len(self.items)
