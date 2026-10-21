# package2/module3.py

from . import class1
from .subpackage1.module5 import function2


def main():
    print(class1())
    print(function2())


if __name__ == "__main__":
    main()
