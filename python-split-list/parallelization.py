"""
Plot the Mandelbrot set using parallel workers.

Usage:
$ python parallelization.py
"""

import functools
import multiprocessing
import os
import time
from dataclasses import dataclass
from math import log
from typing import Callable, Iterable

import numpy as np
from PIL import Image

from splitting.multidimensional import Bounds, split_multi

IMAGE_WIDTH, IMAGE_HEIGHT = 1280, 720
CENTER = -0.7435 + 0.1314j
SCALE = 0.0000025
MAX_ITERATIONS = 256
ESCAPE_RADIUS = 1000
NUM_CHUNKS = os.cpu_count() or 4


class Chunk:
    """A chunk of the image to be computed and rendered."""

    def __init__(self, bounds: Bounds) -> None:
        self.bounds = bounds
        self.height = bounds.size[0]
        self.width = bounds.size[1]
        self.pixels = np.zeros((self.height, self.width), dtype=np.uint8)

    def __getitem__(self, coordinates) -> int:
        """Get the value of a pixel at the given absolute coordinates."""
        return self.pixels[self.bounds.offset(*coordinates)]

    def __setitem__(self, coordinates, value: int) -> None:
        """Set the value of a pixel at the given absolute coordinates."""
        self.pixels[self.bounds.offset(*coordinates)] = value


@dataclass
class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1

    def stability(self, c: complex, smooth=False, clamp=True) -> float:
        value = self.escape_count(c, smooth) / self.max_iterations
        return max(0.0, min(value, 1.0)) if clamp else value

    def escape_count(self, c: complex, smooth=False) -> int | float:
        z = 0 + 0j
        for iteration in range(self.max_iterations):
            z = z**2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return iteration + 1 - log(log(abs(z))) / log(2)
                return iteration
        return self.max_iterations


def timed(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"{function.__name__}() took {end - start:.2f} seconds")
        return result

    return wrapper


def main() -> None:
    for worker in (process_chunks_parallel, process_chunks_sequential):
        image = compute(worker)
        image.show()


@timed
def process_chunks_sequential(chunked_bounds: Iterable[Bounds]) -> list[Chunk]:
    return list(map(generate_chunk, chunked_bounds))


@timed
def process_chunks_parallel(chunked_bounds: Iterable[Bounds]) -> list[Chunk]:
    with multiprocessing.Pool() as pool:
        return pool.map(generate_chunk, chunked_bounds)


def generate_chunk(bounds: Bounds) -> Chunk:
    """Generate a chunk of pixels for the given bounds."""
    chunk = Chunk(bounds)
    mandelbrot_set = MandelbrotSet(MAX_ITERATIONS, ESCAPE_RADIUS)
    for y, x in bounds:
        c = transform(y, x)
        instability = 1 - mandelbrot_set.stability(c, smooth=True)
        chunk[y, x] = int(instability * 255)
    return chunk


def transform(y: int, x: int) -> complex:
    """Transform the given pixel coordinates to the complex plane."""
    im = SCALE * (IMAGE_HEIGHT / 2 - y)
    re = SCALE * (x - IMAGE_WIDTH / 2)
    return complex(re, im) + CENTER


def compute(worker: Callable) -> Image.Image:
    """Render the image using the given worker function."""
    chunks = worker(split_multi(NUM_CHUNKS, IMAGE_HEIGHT, IMAGE_WIDTH))
    return combine(chunks)


def combine(chunks: list[Chunk]) -> Image.Image:
    """Combine the chunks into a single image."""
    pixels = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.uint8)
    for chunk in chunks:
        pixels[chunk.bounds.slices()] = chunk.pixels
    return Image.fromarray(pixels, mode="L")


if __name__ == "__main__":
    main()
