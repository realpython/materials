#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import example


if __name__ == "__main__":
    # sample data for our call:
    x = 6
    y = 2.3

    answer = example.cpp_function(x, y)
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")

