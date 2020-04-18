#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
import pathlib


if __name__ == "__main__":
    # Load the shared library into c types.
    libname = pathlib.Path().absolute() / "libcmult.so"
    c_lib = ctypes.CDLL(libname)

    # Get float return without wrapping
    print("Calling returnDouble with no specified return value:")
    getDouble = c_lib.returnDouble
    answer = getDouble()
    print(f"    In Python: returnDouble: {answer:.2f}")

    print()
    print("This time with the proper return type:")
    getDouble.restype = ctypes.c_double
    answer = getDouble()
    print(f"    In Python: returnDouble: {answer:.2f}")


    # Sample data for our call:
    x, y = 6, 2.3

    # You need tell ctypes that the function returns a float
    print()
    print("Passing and int and a double to C")
    multiply = c_lib.multiply
    multiply.restype = ctypes.c_double
    multiply.argtypes = [ctypes.c_int, ctypes.c_double]
    answer = multiply(x, y)
    print(f"    In Python: multiply: int: {x} double {y:.1f} return val {answer:.1f}")
