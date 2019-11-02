#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
import pathlib


if __name__ == "__main__":
    # load the shared library into c types.
    libname = pathlib.Path().absolute() / "libc_function.so"
    c_lib = ctypes.CDLL(libname)

    # sample data for our call:
    x = 6
    y = 2.3

    # This will not work:
    # answer = c_lib.c_function(6, 2.3)

    # This produces a bad answer:
    answer = c_lib.c_function(6, ctypes.c_float(2.3))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print()

    # You need tell ctypes that the function returns a float
    c_function = c_lib.c_function
    c_function.restype = ctypes.c_float
    answer = c_function(6, ctypes.c_float(2.3))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")

