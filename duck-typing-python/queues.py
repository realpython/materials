from collections import deque


class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    def __iter__(self):
        return iter(self._elements)

    def __len__(self):
        return len(self._elements)

    def __reversed__(self):
        return reversed(self._elements)

    def __contains__(self, element):
        return element in self._elements
