import math
from collections.abc import Sequence

from statkit.descriptive import mean


def pearson(x: Sequence[float], y: Sequence[float]) -> float:
    """Return Pearson's correlation coefficient for x and y."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    if len(x) < 2:
        raise ValueError("pearson requires at least two data points")
    x_mean, y_mean = mean(x), mean(y)
    dx = [xi - x_mean for xi in x]
    dy = [yi - y_mean for yi in y]
    covariance = math.fsum(a * b for a, b in zip(dx, dy))
    spread = math.sqrt(
        math.fsum(a * a for a in dx) * math.fsum(b * b for b in dy)
    )
    if spread == 0:
        raise ValueError("at least one input is constant")
    return covariance / spread


def spearman(x: Sequence[float], y: Sequence[float]) -> float:
    """Return Spearman's rank correlation coefficient for x and y."""
    return pearson(_ranks(x), _ranks(y))


def _ranks(data: Sequence[float]) -> list[float]:
    """Rank data from 1 upward, giving ties the average of their ranks."""
    order = sorted(range(len(data)), key=lambda i: data[i])
    ranks = [0.0] * len(data)
    start = 0
    while start < len(order):
        end = start
        while (
            end + 1 < len(order) and data[order[end + 1]] == data[order[start]]
        ):
            end += 1
        average_rank = (start + end) / 2 + 1
        for position in range(start, end + 1):
            ranks[order[position]] = average_rank
        start = end + 1
    return ranks
