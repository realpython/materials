from PIL import Image

from mandelbrot_03 import MandelbrotSet
from viewport_01 import Viewport

if __name__ == "__main__":

    mandelbrot_set = MandelbrotSet(max_iterations=20)

    image = Image.new(mode="1", size=(512, 512), color=1)
    for pixel in Viewport(image, xmin=-2.5, xmax=1):
        if complex(pixel) in mandelbrot_set:
            pixel.color = 0

    image.show()
