from typing import TypeVar, Union

T = TypeVar('T')
S = TypeVar('S')


def identity(element: T) -> Union[T, S]:
    """Identity function serving as a default key provider."""
    return element
