from mandelbrot_03 import MandelbrotSet
from PIL import Image

if __name__ == "__main__":
    mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)

    width, height = 512, 512
    scale = 0.0075
    GRAYSCALE = "L"

    image = Image.new(mode=GRAYSCALE, size=(width, height))
    for y in range(height):
        for x in range(width):
            re = scale * (x - width / 2)
            im = scale * (height / 2 - y)
            c = complex(re, im)
            instability = 1 - mandelbrot_set.stability(c, smooth=True)
            image.putpixel((x, y), int(instability * 255))

    image.show()
