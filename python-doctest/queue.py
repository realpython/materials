from collections import deque


class Queue:
    def __init__(self):
        """Implement a Queue data type.

        >>> Queue()
        Queue([])

        >>> numbers = Queue()
        >>> numbers
        Queue([])

        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3])
        """
        self._elements = deque()

    def enqueue(self, element):
        """Add items to the right end of the queue.

        >>> numbers = Queue()
        >>> numbers
        Queue([])

        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)

        >>> numbers
        Queue([1, 2, 3])
        """
        self._elements.append(element)

    def dequeue(self):
        """Remove and return an item from the left end of the queue.

        >>> numbers = Queue()
        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)

        >>> numbers
        Queue([1, 2, 3])
        >>> numbers.dequeue()
        1
        >>> numbers.dequeue()
        2
        >>> numbers.dequeue()
        3

        >>> numbers
        Queue([])
        """
        return self._elements.popleft()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({list(self._elements)})"
