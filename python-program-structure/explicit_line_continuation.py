"""Continuing a statement across lines with a backslash.

Code from the "Explicit Line Continuation" section of the tutorial. A
backslash as the very last character on a line tells Python to ignore the
newline that follows it. PEP 8 recommends reaching for this only when
implicit line continuation is not practicable.

The tutorial's three error examples are not reproduced here because they
cannot run: an unterminated 's =', an unterminated 'x = 1 + 2 +', and a
backslash followed by a stray space character.
"""

# fmt: off
s = \
'Hello, World!'
print(repr(s))

x = 1 + 2 \
    + 3 + 4 \
    + 5 + 6
print(x)
# fmt: on
