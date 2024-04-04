class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __reversed__(self):
        return reversed(self.items)
