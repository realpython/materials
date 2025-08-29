import pathlib

BASE_DIR = pathlib.Path(".")
number = 42
fruits = ["apple", "grape", "orange"]


def func(value):
    """A sample docstring."""
    return f"The input value is: {value}"


def main():
    # A sample comment
    func(number)
    for fruit in fruits:
        print(fruit)


if __name__ == "__main__":
    main()
