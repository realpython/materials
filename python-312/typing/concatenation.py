from typing import TypeVar

T = TypeVar("T", str, bytes)


def concatenate(first: T, second: T) -> T:
    return first + second


# %% Python 3.12

# def concatenate[T: (str, bytes)](first: T, second: T) -> T:
#     return first + second
