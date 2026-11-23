"""Conditional expressions, Python's ternary operator.

Code from the "Conditional Expressions (Python's Ternary Operator)" section
of the tutorial. Where the REPL echoed a value, the script calls print().
"""

raining = False
print("Let's go to the", "beach" if not raining else "library")
raining = True
print("Let's go to the", "beach" if not raining else "library")

age = 12
s = "minor" if age < 21 else "adult"
print(repr(s))

print(repr("yes" if ("qux" in ["foo", "bar", "baz"]) else "no"))

# Finding the larger of two numbers with an if statement...
a = 5
b = 8
if a > b:
    m = a
else:
    m = b
print(m)

# ...and with a conditional expression.
m = a if a > b else b
print(m)

# The conditional expression has lower precedence than + ...
x = y = 40
z = 1 + x if x > y else y + 2
print(z)
z = (1 + x) if x > y else (y + 2)
print(z)

# ...so group it with parentheses to evaluate it first.
z = 1 + (x if x > y else y) + 2
print(z)

# Short-circuit evaluation: the 1 / 0 terms are never evaluated.
print(repr("foo" if True else 1 / 0))
print(repr(1 / 0 if False else "bar"))

# Chained conditional expressions.
x = 3
# fmt: off
s = ("foo" if (x == 1) else
     "bar" if (x == 2) else
     "baz" if (x == 3) else
     "qux" if (x == 4) else
     "quux"
)
# fmt: on
print(repr(s))
