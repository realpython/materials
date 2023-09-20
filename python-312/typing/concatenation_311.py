from typing import TypeVar

T = TypeVar("T", str, bytes)


def concatenate(first: T, second: T) -> T:
    return first + second
