from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()


# %% Python 3.12

# from collections import deque
#
#
# class Queue[T]:
#     def __init__(self) -> None:
#         self.elements: deque[T] = deque()
#
#     def push(self, element: T) -> None:
#         self.elements.append(element)
#
#     def pop(self) -> T:
#         return self.elements.popleft()
