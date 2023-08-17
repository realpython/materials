cpdef int fib(int n):
    with nogil:
        return _fib(n)


cdef int _fib(int n) noexcept nogil:
    return n if n < 2 else _fib(n - 2) + _fib(n - 1)

