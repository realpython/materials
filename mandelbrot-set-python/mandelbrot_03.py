# mandelbrot_03.py

from math import log
from typing import NamedTuple


class MandelbrotSet(NamedTuple):
    max_iterations: int

    def __contains__(self, c: complex) -> bool:
        return self.probability(c) == 1

    def probability(self, c: complex, smooth: bool = False) -> float:
        return self.escape_count(c, smooth) / self.max_iterations

    def escape_count(self, c: complex, smooth: bool = False) -> int:
        z = 0
        for i in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) >= 2:
                return i + 1 - log(log(abs(z))) / log(2) if smooth else i
        return self.max_iterations
