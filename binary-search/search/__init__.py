from typing import Callable, TypeVar, Union

T = TypeVar("T")
S = TypeVar("S")

Key = Callable[[T], Union[T, S]]


def identity(element: T) -> Union[T, S]:
    """Identity function serving as a default key provider."""
    return element
