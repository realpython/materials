from PIL import Image
from PIL.ImageColor import getrgb

from mandelbrot_03 import MandelbrotSet
from viewport import Viewport


def hsb(hue_degrees: int, saturation: float, brightness: float):
    return getrgb(
        f"hsv({hue_degrees % 360},"
        f"{saturation * 100}%,"
        f"{brightness * 100}%)"
    )


if __name__ == "__main__":
    print("This might take a while...")

    mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)
    image = Image.new(mode="RGB", size=(512, 512))
    for pixel in Viewport(image, center=-0.75, width=3.5):
        stability = mandelbrot_set.stability(complex(pixel), smooth=True)
        pixel.color = (
            (0, 0, 0)
            if stability == 1
            else hsb(
                hue_degrees=int(stability * 360),
                saturation=stability,
                brightness=1,
            )
        )

    image.show()
