# parallel/__init__.py

import ctypes
import pathlib
import threading

import numpy as np

# Load the compiled C library
library_path = str(pathlib.Path(__file__).parent / f"{__package__}.so")
library = ctypes.CDLL(library_path)

# Define a C data type for "unsigned char*"
UnsignedByteArrayPointer = ctypes.POINTER(ctypes.c_ubyte)

# Define a prototype for the C function
library.process.argtypes = [
    UnsignedByteArrayPointer,  # unsigned char* pixels
    ctypes.c_int,  # int length
    ctypes.c_int,  # int offset
    ctypes.c_float,  # float ev
    ctypes.c_float,  # float gamma
]


# Define a wrapper function accessible from Python
def process(pixels: np.ndarray, ev: float, gamma: float) -> None:
    pointer = pixels.ctypes.data_as(UnsignedByteArrayPointer)
    threads = [
        threading.Thread(
            target=library.process,
            args=(pointer, pixels.size, offset, ev, gamma),
        )
        for offset in range(3)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
