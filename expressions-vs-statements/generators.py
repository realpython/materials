import random


def main():
    lf = lowpass_filter()
    lf.send(None)
    for value in generate_noise(10):
        print(f"{value:>5.2f}: {lf.send(value):>5.2f}")


def generate_noise(size):
    for _ in range(size):
        yield 2 * random.random() - 1


def lowpass_filter():
    a = yield
    b = yield a
    while True:
        a, b = b, (yield (a + b) / 2)


if __name__ == "__main__":
    main()
