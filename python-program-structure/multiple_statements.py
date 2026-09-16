"""Putting several statements on one line with semicolons.

Code from the "Multiple Statements Per Line" section of the tutorial.
Python allows it, PEP 8 expressly discourages it, and Ruff flags it as
E702 -- which is exactly the tutorial's point, so the warnings are
suppressed rather than the examples rewritten.
"""

# fmt: off
x = 1; y = 2; z = 3  # noqa: E702
print(x); print(y); print(z)  # noqa: E702

# The same result, written the way a Python programmer normally would.
x, y, z = 1, 2, 3
print(x, y, z, sep='\n')
# fmt: on
