from typing import Callable


def add_one(i: int) -> int:
    return i + 1


def multiply_with(x: int, y: int) -> int:
    return x * y


def as_pixels(i: int) -> str:
    return f"{i}px"


def calculate(i: int, action: Callable[..., int], *args: int) -> int:
    return action(i, *args)


# Works:
calculate(1, add_one)
calculate(1, multiply_with, 3)

# Doesn't work:
calculate(1, 3)
calculate(1, as_pixels)
