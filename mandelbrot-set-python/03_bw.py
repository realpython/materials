from PIL import Image

from mandelbrot_01 import MandelbrotSet

if __name__ == "__main__":

    mandelbrot_set = MandelbrotSet(max_iterations=20)

    width, height = 512, 512
    scale = 0.0075
    black_and_white = "1"

    image = Image.new(mode=black_and_white, size=(width, height))
    for y in range(height):
        for x in range(width):
            re = scale * (x - width / 2)
            im = scale * (height / 2 - y)
            image.putpixel((x, y), complex(re, im) not in mandelbrot_set)

    image.show()
