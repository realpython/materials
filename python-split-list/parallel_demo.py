"""
Synthesize an image in chunks using parallel workers.

Usage:
$ python parallel_demo.py
"""

import functools
import multiprocessing
import time
from dataclasses import dataclass
from math import log
from os import cpu_count
from typing import Callable, Iterable, Iterator

import numpy as np
from PIL import Image
from spatial_splitting import Bounds, split_multi

IMAGE_WIDTH, IMAGE_HEIGHT = 1920, 1080
CENTER = -0.7435 + 0.1314j
SCALE = 0.0000015
MAX_ITERATIONS = 256
ESCAPE_RADIUS = 1000
NUM_CHUNKS = cpu_count() or 4


class Chunk:
    """A chunk of the image to be computed and rendered."""

    def __init__(self, bounds: Bounds) -> None:
        self.bounds = bounds
        self.height = bounds.size[0]
        self.width = bounds.size[1]
        self.pixels = np.zeros((self.height, self.width), dtype=np.uint8)

    def __getitem__(self, coordinates: tuple[int, int]) -> int:
        return self.pixels[self.bounds.offset(*coordinates)]

    def __setitem__(self, coordinates: tuple[int, int], value: int) -> None:
        self.pixels[self.bounds.offset(*coordinates)] = value


@dataclass
class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c):
        return self.stability(c) == 1

    def stability(self, c, smooth=False, clamp=True):
        value = self.escape_count(c, smooth) / self.max_iterations
        return max(0.0, min(value, 1.0)) if clamp else value

    def escape_count(self, c, smooth=False):
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = z**2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return iteration + 1 - log(log(abs(z))) / log(2)
                return iteration
        return self.max_iterations


def transform(y: int, x: int) -> complex:
    """Transform the given pixel coordinates to the complex plane."""
    im = SCALE * (IMAGE_HEIGHT / 2 - y)
    re = SCALE * (x - IMAGE_WIDTH / 2)
    return complex(re, im) + CENTER


def generate_chunk(bounds: Bounds) -> Chunk:
    """Generate a chunk of pixels for the given bounds."""
    chunk = Chunk(bounds)
    mandelbrot_set = MandelbrotSet(MAX_ITERATIONS, ESCAPE_RADIUS)
    for y, x in bounds:
        c = transform(y, x)
        instability = 1 - mandelbrot_set.stability(c, smooth=True)
        chunk[y, x] = int(instability * 255)
    return chunk


def combine(chunks: Iterable[Chunk]) -> Image.Image:
    """Combine the chunks into a single image."""
    pixels = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.uint8)
    for chunk in chunks:
        pixels[chunk.bounds.slices()] = chunk.pixels
    return Image.fromarray(pixels, mode="L")


def timed(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"{function.__name__}() took {end - start:.2f} seconds")
        return result

    return wrapper


def process_sequentially(bounds_iter: Iterator[Bounds]) -> Iterator[Chunk]:
    return map(generate_chunk, bounds_iter)


def process_in_parallel(bounds_iter: Iterator[Bounds]) -> list[Chunk]:
    with multiprocessing.Pool() as pool:
        return pool.map(generate_chunk, bounds_iter)


@timed
def compute(worker: Callable) -> Image.Image:
    return combine(worker(split_multi(NUM_CHUNKS, IMAGE_HEIGHT, IMAGE_WIDTH)))


def main() -> None:
    for worker in (process_sequentially, process_in_parallel):
        compute(worker).show()


if __name__ == "__main__":
    main()
