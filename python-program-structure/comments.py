"""Attaching explanatory detail to code with the hash character.

Code from the "Comments" section of the tutorial. The interpreter ignores
everything from a '#' to the end of that line, unless the '#' is inside a
string literal.

The tutorial's backslash-plus-comment example is not reproduced here: a
comment cannot follow an explicit line continuation, so it raises a
SyntaxError.
"""

# fmt: off
a = ['foo', 'bar', 'baz']  # I am a comment.
print(a)

# I am a comment.
    # I am too.

# A hash inside a string literal is protected and starts no comment.
a = 'foobar # I am *not* a comment.'
print(repr(a))

# Calculate and display the area of a circle.

pi = 3.1415926536
r = 12.35

area = pi * (r ** 2)

print('The area of a circle with radius', r, 'is', area)

# Comments can be included within implicit line continuation.
x = (1 + 2           # I am a comment.
     + 3 + 4         # Me too.
     + 5 + 6)
print(x)

a = [
    'foo', 'bar',    # Me three.
    'baz', 'qux'
]
print(a)

# Python has no block comment syntax, so a multiline comment is just a run
# of hash-prefixed lines:

# Initialize value for radius of circle.
#
# Then calculate the area of the circle
# and display the result to the console.

pi = 3.1415926536
r = 12.35

area = pi * (r ** 2)

print('The area of a circle with radius', r, 'is', area)
# fmt: on
