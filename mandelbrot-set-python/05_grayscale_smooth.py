from PIL import Image

from mandelbrot_03 import MandelbrotSet

if __name__ == "__main__":

    mandelbrot_set = MandelbrotSet(max_iterations=20)

    width, height = 512, 512
    scale = 0.0075
    grayscale = "L"

    image = Image.new(mode=grayscale, size=(width, height))
    for y in range(height):
        for x in range(width):
            re = scale * (x - width / 2)
            im = scale * (height / 2 - y)
            c = complex(re, im)
            stability = 1 - mandelbrot_set.stability(c, smooth=True)
            image.putpixel((x, y), int(stability * 255))

    image.show()
