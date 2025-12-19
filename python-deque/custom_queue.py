from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        try:
            return self._items.popleft()
        except IndexError:
            # Break exception chain to hide implementation details
            raise IndexError("dequeue from an empty queue") from None

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        yield from self._items

    def __reversed__(self):
        yield from reversed(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"


if __name__ == "__main__":
    queue = Queue()
    print("Enqueueing items with '.enqueue()'...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print("Dequeueing one item with '.dequeue()'...")
    print(queue.dequeue())
    print(queue)
