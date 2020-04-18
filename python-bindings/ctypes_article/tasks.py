""" Task definitions for invoke command line utility for python bindings
    ctypes article. """
import invoke
import pathlib


@invoke.task
def clean(c):
    """ Remove any built objects """
    for pattern in ["*.o", "*.so", ]:
        c.run("rm -rf {}".format(pattern))


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task
def build_buf_serialize(c):
    """ Build the shared library for the sample C code """
    print_banner("Building Buf Serialize C Library")
    invoke.run("gcc -shared -o libbuf_serialize.so -Wall -Werror -fpic buf_serialize.c -I /usr/include/python3.7")
    print("* Complete")


@invoke.task(build_buf_serialize)
def test(c):
    """ Run the script to test ctypes """
    print_banner("Testing ctypes Module")
    invoke.run("python3 test_serialize.py", pty=True)


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
def test_ctypes(c):
    """ Run the script to test ctypes """
    print_banner("Testing wrapped ctypes function")
    invoke.run("python3 ctypes_wrapped.py", pty=True)


