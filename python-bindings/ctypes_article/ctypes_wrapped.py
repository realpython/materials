#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
import pathlib

def wrap_function(lib, funcname, restype, argtypes):
    ''' Simplify wrapping ctypes functions '''
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

if __name__ == "__main__":
    # Load the shared library into c types.
    libname = pathlib.Path().absolute() / "libcmult.so"
    c_lib = ctypes.CDLL(libname)

    # Sample data for our call:
    x, y = 6, 2.3

    # You need tell ctypes that the function returns a float
    print()
    print("Passing and int and a double to wrapped C function")
    multiply = wrap_function(c_lib, "multiply", ctypes.c_double,
                             [ctypes.c_int, ctypes.c_double])
    answer = multiply(x, y)
    print(f"    In Python: multiply: int: {x} double {y:.1f} return val {answer:.1f}")
