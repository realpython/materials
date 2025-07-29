from typing import Annotated


def fib(n: int) -> int:
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def increment(x: Annotated[int, fib(35)]) -> int:
    return x + 1
