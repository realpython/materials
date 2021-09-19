from PIL import Image
from PIL.ImageColor import getrgb

from mandelbrot_03 import MandelbrotSet
from viewport_02 import Viewport


def hsb(hue_degrees: int, saturation: float, brightness: float):
    return getrgb(
        f"hsv({hue_degrees % 360},"
        f"{saturation * 100}%,"
        f"{brightness * 100}%)"
    )


if __name__ == "__main__":
    print("This might take a while...")

    mandelbrot_set = MandelbrotSet(max_iterations=25)
    image = Image.new(mode="RGB", size=(512, 512))
    for pixel in Viewport(image, center=-0.75, width=3.5):
        p = mandelbrot_set.probability(complex(pixel), smooth=True)
        probability = max(0, min(p, 1))
        pixel.color = (
            (0, 0, 0)
            if probability == 1
            else hsb(
                hue_degrees=int(probability * 360),
                saturation=probability,
                brightness=1,
            )
        )

    image.show()
