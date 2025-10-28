from collections import deque


def tail(filename, lines=10):
    try:
        with open(filename) as file:
            return deque(file, lines)
    except OSError as error:
        print(f'Opening file "{filename}" failed with error: {error}')
