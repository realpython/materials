from PIL import Image
from PIL import ImageEnhance

from mandelbrot_03 import MandelbrotSet
from viewport_02 import Viewport

if __name__ == "__main__":
    print("This might take a while...")

    mandelbrot_set = MandelbrotSet(max_iterations=256)

    image = Image.new(mode="L", size=(512, 512))
    for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
        c = complex(pixel)
        probability = 1 - mandelbrot_set.probability(c, smooth=True)
        pixel.color = max(0, min(int(probability * 255), 255))

    enhancer = ImageEnhance.Brightness(image)
    enhancer.enhance(1.25).show()
