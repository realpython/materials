from collections.abc import Iterable
from typing import Any


def average(numbers: list[int | float]) -> float:
    if not numbers:
        raise ValueError("average() requires at least one number")
    return sum(numbers) / len(numbers)


def median(values: Any, sort=False):
    values = sorted(values) if sort else values
    return values[(len(values) - 1) // 2]


def count(values: Iterable[int | None]):
    return sum(1 if v is not None else 0 for v in values)
