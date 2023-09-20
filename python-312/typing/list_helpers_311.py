from typing import TypeVar

T = TypeVar("T")


def push_and_pop(elements: list[T], element: T) -> T:
    elements.append(element)
    return elements.pop(0)
