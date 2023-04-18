class Stack:
    def __init__(self, items=None):
        if items is None:
            self._items = []
        else:
            self._items = list(items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._items})"


class StackInheritance(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        return super().pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({super().__repr__()})"
