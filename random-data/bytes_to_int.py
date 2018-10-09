"""
Demonstration of how `int.from_bytes()` converts a Python bytes obj to int.
Used in random module's `SystemRandom.random()` to generate a float in
[0.0, 1.0) from `os.urandom()`:
https://github.com/python/cpython/blob/c6040638aa1537709add895d24cdbbb9ee310fde/Lib/random.py#L676

An example: the number 1984 can be "decomposed" in the decimal system (base 10)
as (1 * 10 ** 3)
 + (9 * 10 ** 2)
 + (8 * 10 ** 1)
 + (4 * 10 ** 0)

`int.from_bytes()` (with big endianness) uses a base-256 numbering system
Given b = b'\xe6\x04\x00\x00',
>>> list(b)
[230, 4, 0, 0]
And the int is then
   (230 * 256 ** 3)
 + (4   * 256 ** 2)
 + (0   * 256 ** 1)
 + (0   * 256 ** 0) == 3859021824
"""

import os
import random


def bytes_to_int(b: bytes, byteorder: str = "big") -> int:
    if byteorder == "big":
        return sum(j * 256 ** i for i, j in enumerate(b[::-1]))
    elif byteorder == "little":
        return sum(j * 256 ** i for i, j in enumerate(b))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'.")


def test(seed=None):
    for _ in range(10):
        b = os.urandom(random.randint(0, 100))
        assert bytes_to_int(b, "big") == int.from_bytes(b, "big"), b
        assert bytes_to_int(b, "little") == int.from_bytes(b, "little"), b


if __name__ == "__main__":
    import sys

    sys.exit(test())
