from collections import deque


def tail(filename, lines=10):
    try:
        with open(filename) as file:
            return deque(file, maxlen=lines)
    except OSError as error:
        print(f'Opening file "{filename}" failed with error: {error}')


if __name__ == "__main__":
    print(tail("./README.md"))
