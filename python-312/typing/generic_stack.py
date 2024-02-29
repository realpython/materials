from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.stack: list[T] = []

    def push(self, element: T) -> None:
        self.stack.append(element)

    def pop(self) -> T:
        return self.stack.pop()


# %% Python 3.12

# class Stack[T]:
#     def __init__(self) -> None:
#         self.stack: list[T] = []
#
#     def push(self, element: T) -> None:
#         self.stack.append(element)
#
#     def pop(self) -> T:
#         return self.stack.pop()
