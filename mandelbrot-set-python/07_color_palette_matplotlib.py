import matplotlib.cm
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

    colormap = matplotlib.cm.get_cmap("twilight").colors
    palette = denormalize(colormap)

    mandelbrot_set = MandelbrotSet(max_iterations=512, escape_radius=1000)
    image = Image.new(mode="RGB", size=(512, 512))
    viewport = Viewport(image, center=-0.7435 + 0.1314j, width=0.002)
    paint(mandelbrot_set, viewport, palette, smooth=True)
    image.show()
