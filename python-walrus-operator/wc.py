import pathlib
import sys


def count_words_1(filenames):
    for filename in filenames:
        path = pathlib.Path(filename)
        counts = (
            path.read_text().count("\n"),  # Number of lines
            len(path.read_text().split()),  # Number of words
            len(path.read_text()),  # Number of characters
        )
        print(*counts, path)


def count_words_2(filenames):
    for filename in filenames:
        path = pathlib.Path(filename)
        counts = (
            (text := path.read_text()).count("\n"),  # Number of lines
            len(text.split()),  # Number of words
            len(text),  # Number of characters
        )
        print(*counts, path)


def count_words_3(filenames):
    for filename in filenames:
        path = pathlib.Path(filename)
        text = path.read_text()
        counts = (
            text.count("\n"),  # Number of lines
            len(text.split()),  # Number of words
            len(text),  # Number of characters
        )
        print(*counts, path)


if __name__ == "__main__":
    count_words_1(sys.argv[1:])
    count_words_2(sys.argv[1:])
    count_words_3(sys.argv[1:])
