# mandelbrot_01.py

from typing import NamedTuple


class MandelbrotSet(NamedTuple):
    max_iterations: int

    def __contains__(self, c: complex) -> bool:
        z = 0
        for _ in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) >= 2:
                return False
        return True
