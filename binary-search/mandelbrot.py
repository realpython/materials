"""
Visualize the Mandelbrot set.

Usage:
$ pip install Pillow
$ python mandelbrot.py image.png
"""

import argparse
from PIL import Image


class Rect:
    def __init__(self, x0, x1, y0, y1) -> None:
        self.x0, self.x1 = x0, x1
        self.y0, self.y1 = y0, y1

    @property
    def width(self) -> int:
        return self.x1 - self.x0

    @property
    def height(self) -> int:
        return self.y1 - self.y0

    @property
    def aspect_ratio(self) -> float:
        return self.height / self.width


def main(args: argparse.Namespace) -> None:
    """Script entry point."""
    image = draw(bbox=Rect(-2.2, 0.8, -1.25, 1.25), width=1280, iterations=20)
    image.save(args.path)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser.parse_args()


def draw(bbox: Rect, width: int, iterations: int) -> Image:
    """Return an image instance."""

    height = int(width * bbox.aspect_ratio)
    image = Image.new('L', (width, height))

    for y in range(height):
        for x in range(width):
            re = x * bbox.width / width + bbox.x0
            im = (height - y) * bbox.height / height + bbox.y0
            color = 255 - int(255 * divergence(complex(re, im), iterations))
            image.putpixel((x, y), color)

    return image


def divergence(number: complex, max_iterations: int, limit: int = 2) -> float:
    """Return Mandelbrot set membership as a value between 0 and 1 inclusive."""
    z = 0j
    for _ in range(max_iterations):
        z = z**2 + number
        if abs(z) > limit:
            return 0
    return abs(z) / limit


if __name__ == '__main__':
    main(parse_args())
