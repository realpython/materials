import math
from collections.abc import Sequence


def mean(data: Sequence[float]) -> float:
    """Return the arithmetic mean of data."""
    if not data:
        raise ValueError("mean requires at least one data point")
    return math.fsum(data) / len(data)


def median(data: Sequence[float]) -> float:
    """Return the middle value of data, averaging the two middle values."""
    if not data:
        raise ValueError("median requires at least one data point")
    values = sorted(data)
    middle = len(values) // 2
    if len(values) % 2 == 1:
        return values[middle]
    return (values[middle - 1] + values[middle]) / 2


def stdev(data: Sequence[float]) -> float:
    """Return the sample standard deviation of data."""
    if len(data) < 2:
        raise ValueError("stdev requires at least two data points")
    center = mean(data)
    squares = math.fsum((x - center) ** 2 for x in data)
    return math.sqrt(squares / (len(data) - 1))
