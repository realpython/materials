#!/usr/bin/env python
import cython_example

# Sample data for our call
x, y = 6, 2.3

answer = cython_example.pymult(x, y)
print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
