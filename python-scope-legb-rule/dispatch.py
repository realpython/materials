from sys import platform


def linux_print():
    print("Printing from Linux...")


def win32_print():
    print("Printing from Windows...")


def darwin_print():
    print("Printing from macOS...")


printer = globals()[platform + "_print"]

printer()
