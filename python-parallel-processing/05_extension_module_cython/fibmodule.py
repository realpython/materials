import cython


@cython.ccall
def fib(n: cython.int) -> cython.int:
    with cython.nogil:
        return _fib(n)


@cython.cfunc
@cython.nogil
@cython.exceptval(check=False)
def _fib(n: cython.int) -> cython.int:
    return n if n < 2 else _fib(n - 2) + _fib(n - 1)


if cython.compiled:
    print("Cython compiled this module")
else:
    print("Cython didn't compile this module")
