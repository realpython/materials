""" Task definitions for invoke command line utility for python bindings
    overview article. """
import cffi
import invoke
import pathlib


@invoke.task
def clean(c):
    """ Remove any built objects """
    for pattern in ["*.o", "*.so", "cffi_example* cython_wrapper.cpp"]:
        c.run("rm -rf {}".format(pattern))


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task
def build_cmult(c):
    """ Build the shared library for the sample C code """
    print_banner("Building C Library")
    invoke.run("gcc -c -Wall -Werror -fpic cmult.c -I /usr/include/python3.7")
    invoke.run("gcc -shared -o libcmult.so cmult.o")
    print("* Complete")


@invoke.task(build_cmult)
def test_ctypes(c):
    """ Run the script to test ctypes """
    print_banner("Testing ctypes Module")
    invoke.run("python3 ctypes_test.py", pty=True)


@invoke.task(build_cmult)
def build_cffi(c):
    """ Build the CFFI Python bindings """
    print_banner("Building CFFI Module")
    ffi = cffi.FFI()

    this_dir = pathlib.Path().absolute()
    h_file_name = this_dir / "cmult.h"
    with open(h_file_name) as h_file:
        ffi.cdef(h_file.read())

    ffi.set_source(
        "cffi_example",
        # Since we are calling a fully built library directly no custom source
        # is necessary. We need to include the .h files, though, because behind
        # the scenes cffi generates a .c file which contains a Python-friendly
        # wrapper around each of the functions.
        '#include "cmult.h"',
        # The important thing is to include the pre-built lib in the list of
        # libraries we are linking against:
        libraries=["cmult"],
        library_dirs=[this_dir.as_posix()],
        extra_link_args=["-Wl,-rpath,."],
    )

    ffi.compile()
    print("* Complete")


@invoke.task()
def test_cffi(c):
    """ Run the script to test CFFI """
    print_banner("Testing CFFI Module")
    invoke.run("python3 cffi_test.py", pty=True)


@invoke.task()
def build_cppmult(c):
    """ Build the shared library for the sample C++ code """
    print_banner("Building C++ Library")
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppmult.cpp "
        "-o libcppmult.so "
    )
    print("* Complete")


def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
        "`python3 -m pybind11 --includes` "
        "-I /usr/include/python3.7 -I .  "
        "{0} "
        "-o {1}`python3.7-config --extension-suffix` "
        "-L. -lcppmult -Wl,-rpath,.".format(cpp_name, extension_name)
    )


@invoke.task(build_cppmult)
def build_pybind11(c):
    """ Build the pybind11 wrapper library """
    print_banner("Building PyBind11 Module")
    compile_python_module("pybind11_wrapper.cpp", "pybind11_example")
    print("* Complete")


@invoke.task()
def test_pybind11(c):
    """ Run the script to test PyBind11 """
    print_banner("Testing PyBind11 Module")
    invoke.run("python3 pybind11_test.py", pty=True)


@invoke.task(build_cppmult)
def build_cython(c):
    """ Build the cython extension module """
    print_banner("Building Cython Module")
    # Run cython on the pyx file to create a .cpp file
    invoke.run("cython --cplus -3 cython_example.pyx -o cython_wrapper.cpp")

    # Compile and link the cython wrapper library
    compile_python_module("cython_wrapper.cpp", "cython_example")
    print("* Complete")


@invoke.task()
def test_cython(c):
    """ Run the script to test Cython """
    print_banner("Testing Cython Module")
    invoke.run("python3 cython_test.py", pty=True)


@invoke.task(
    clean,
    build_cmult,
    test_ctypes,
    build_cffi,
    test_cffi,
    build_pybind11,
    test_pybind11,
    build_cython,
    test_cython,
)
def all(c):
    """ Build and run all tests """
    pass
