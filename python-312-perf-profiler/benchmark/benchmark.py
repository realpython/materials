import sys
import sysconfig
from math import exp, log
from statistics import mean

from PIL import Image


def check_perf_support():
    if sys.version_info < (3, 12):
        version = sysconfig.get_python_version()
        raise RuntimeError(f"This is Python {version}, not 3.12 or later")

    if not sysconfig.get_config_var("PY_HAVE_PERF_TRAMPOLINE"):
        raise RuntimeError("Python doesn't support perf on this platform")

    if not sys.is_stack_trampoline_active():
        raise RuntimeError("Did you forget the '-X perf' option?")

    cflags = sysconfig.get_config_var("CONFIGURE_CFLAGS")
    if "-fno-omit-frame-pointer" not in cflags:
        print("Python compiled without the frame pointer", file=sys.stderr)


def main():
    image = Image.open("image.jpg")
    print("luminance =", get_average_luminance(image.getdata()))
    image.show()


def get_average_luminance(pixels):
    return exp(mean(log(luminance(pixel) + 1e-9) for pixel in pixels))


def luminance(pixel):
    red, green, blue = tuple(linearize(c) for c in pixel)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def linearize(channel, gamma=2.2):
    return (channel / 255) ** gamma


if __name__ == "__main__":
    try:
        check_perf_support()
    except RuntimeError as error:
        print(error, file=sys.stderr)
    else:
        main()
