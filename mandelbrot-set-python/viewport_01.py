# viewport_01.py

from typing import NamedTuple

from PIL import Image


class Viewport(NamedTuple):
    image: Image.Image
    xmin: float
    xmax: float

    @property
    def width(self):
        return self.xmax - self.xmin

    @property
    def height(self):
        return self.width * self.aspect_ratio

    @property
    def aspect_ratio(self):
        return self.image.height / self.image.width

    @property
    def scale(self):
        return self.width / self.image.width

    def __iter__(self):
        for y in range(self.image.height):
            for x in range(self.image.width):
                yield Pixel(self, x, y)


class Pixel(NamedTuple):
    viewport: Viewport
    x: int
    y: int

    @property
    def color(self):
        return self.viewport.image.getpixel((self.x, self.y))

    @color.setter
    def color(self, value):
        self.viewport.image.putpixel((self.x, self.y), value)

    def __complex__(self):
        return complex(
            self.viewport.scale * self.x + self.viewport.xmin,
            self.viewport.scale * (self.viewport.image.height / 2 - self.y),
        )
