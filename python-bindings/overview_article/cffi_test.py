#!/usr/bin/env python3
# IDE might complain with "no module found" here, even when it exists
import cffi_example

if __name__ == "__main__":
    # Sample data for our call:
    x, y = 6, 2.3

    answer = cffi_example.lib.cmult(x, y)
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
