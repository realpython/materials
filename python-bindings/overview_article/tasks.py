""" Task definitions for invoke command line utility for python bindings
    overview article. """
import cffi
import invoke
import os
import pathlib

COMPILE = "gcc -c -Wall -Werror -fpic cmult.c -I /usr/include/python3.7"
LINK = "gcc -shared -o libcmult.so cmult.o"


@invoke.task
def clean(c):
    """ Remove any built objects. """
    for pattern in ["*.o", "*.so", "cffi_example*", ]:
        c.run("rm -rf {}".format(pattern))

@invoke.task
def build_cmult(c):
    """ Compile and link the shared library (DLL) for the sample C++ code."""
    invoke.run(COMPILE)
    invoke.run(LINK)


@invoke.task(build_cmult)
def test_ctypes(c):
    invoke.run("python3 ctypes_test.py", pty=True)

@invoke.task(build_cmult)
def build_cffi(c):
    ffi = cffi.FFI()

    this_dir = pathlib.Path().absolute()
    h_file_name = this_dir / "cmult.h"
    with open(h_file_name) as h_file:
        ffi.cdef(h_file.read())

    ffi.set_source("cffi_example",
        # Since we are calling a fully built library directly no custom source
        # is necessary. We need to include the .h files, though, because behind
        # the scenes cffi generates a .c file which contains a Python-friendly
        # wrapper around each of the functions.
        '#include "cmult.h"',
        # The important thing is to include the pre-built lib in the list of
        # libraries we are linking against:
        libraries=["cmult"],
        library_dirs=[this_dir.as_posix(),],
        extra_link_args=['-Wl,-rpath,.'],
    )

    ffi.compile()

@invoke.task()
def test_cffi(c):
    invoke.run("python3 cffi_test.py", pty=True)

@invoke.task()
def build_pybind11(c):
    """ Compile and link the shared library (DLL) for the sample C++ code."""
    # compile and link the cmult c++ library
    invoke.run("g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
               "cppmult.cpp -o libcppmult.so "
              )
    # compile and link the pybind11 wrapper library
    invoke.run("g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
               "`python3 -m pybind11 --includes` "
               "-I /usr/include/python3.7 -I . "
               "pybind11_wrapper.cpp "
               "-o pybind11_example`python3.7-config --extension-suffix` "
               "-L. -lcppmult -Wl,-rpath,. "
              )

@invoke.task()
def test_pybind11(c):
    invoke.run("python3 pybind11_test.py", pty=True)

@invoke.task(clean, build_cmult, test_ctypes, build_cffi, test_cffi,
             build_pybind11, test_pybind11)
def all(c):
    pass

