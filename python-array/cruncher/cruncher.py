from array import array
from ctypes import POINTER, c_int, c_uint, cdll

cruncher = cdll.LoadLibrary("./cruncher.so")
cruncher.increment.argtypes = (POINTER(c_int), c_uint)
cruncher.increment.restype = None

python_array = array("i", [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1])
c_array = (c_int * len(python_array)).from_buffer(python_array)
cruncher.increment(c_array, len(c_array))

print(python_array)
