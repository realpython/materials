"""Using pass as a placeholder where a statement is syntactically required.

The fixed version of foo.py from "The Python pass Statement" section of the
tutorial. Without the pass line, the empty if block raises an
IndentationError, so that version isn't reproduced here.
"""

if True:
    pass

print("foo")
