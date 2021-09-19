# mandelbrot_02.py

from typing import NamedTuple


class MandelbrotSet(NamedTuple):
    max_iterations: int

    def __contains__(self, c: complex) -> bool:
        return self.probability(c) == 1

    def probability(self, c: complex) -> float:
        return self.escape_count(c) / self.max_iterations

    def escape_count(self, c: complex) -> int:
        z = 0
        for i in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) >= 2:
                return i
        return self.max_iterations
