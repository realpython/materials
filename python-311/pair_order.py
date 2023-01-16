from typing import TypeVar

T0 = TypeVar("T0")
T1 = TypeVar("T1")


def flip(pair: tuple[T0, T1]) -> tuple[T1, T0]:
    first, second = pair
    return (second, first)


pair = ("one", "two")
print(f"{pair} -> {flip(pair)}")
