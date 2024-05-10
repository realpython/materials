from mandelbrot_03 import MandelbrotSet
from PIL import Image
from viewport import Viewport


def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]


def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color) for color in palette
    ]


if __name__ == "__main__":
    print("This might take a while...")

    exterior = [(1, 1, 1)] * 50
    interior = [(1, 1, 1)] * 5
    gray_area = [(1 - i / 44,) * 3 for i in range(45)]
    palette = denormalize(exterior + gray_area + interior)

    mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)
    image = Image.new(mode="RGB", size=(512, 512))
    viewport = Viewport(image, center=-0.75, width=3.5)
    paint(mandelbrot_set, viewport, palette, smooth=True)
    image.show()
