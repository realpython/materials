#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
import pathlib
import sys

if __name__ == "__main__":
    # Load the shared library into c types.
    lib_ext = ".dll" if sys.platform.startswith("win") else ".so"
    libname = pathlib.Path() / f"cmult{lib_ext}"
    c_lib = ctypes.CDLL(libname.resolve().__str__())

    # Sample data for our call:
    x, y = 6, 2.3

    # This will not work:
    # answer = c_lib.cmult(x, y)

    # This produces a bad answer:
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print()

    # You need tell ctypes that the function returns a float
    c_lib.cmult.restype = ctypes.c_float
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
