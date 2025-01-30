import sys

from snakesay import snake


def main():
    snake.say(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
