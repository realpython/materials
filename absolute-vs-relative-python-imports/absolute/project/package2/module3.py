# package2/module3.py

from package2 import class1
from package2.subpackage1.module5 import function2


def main():
    print(class1())
    print(function2())


if __name__ == "__main__":
    main()
