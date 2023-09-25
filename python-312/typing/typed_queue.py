from collections import deque


class IntegerQueue:
    def __init__(self) -> None:
        self.elements: deque[int] = deque()

    def push(self, element: int) -> None:
        self.elements.append(element)

    def pop(self) -> int:
        return self.elements.popleft()


class StringQueue:
    def __init__(self) -> None:
        self.elements: deque[str] = deque()

    def push(self, element: str) -> None:
        self.elements.append(element)

    def pop(self) -> str:
        return self.elements.popleft()
