"""Choosing between alternatives with else and elif.

Code from "The else and elif Clauses" section of the tutorial.
"""

# else: exactly one of the two suites runs.
x = 20
if x < 50:
    print("(first suite)")
    print("x is small")
else:
    print("(second suite)")
    print("x is large")

x = 120
if x < 50:
    print("(first suite)")
    print("x is small")
else:
    print("(second suite)")
    print("x is large")

# elif: Python runs the suite of the first condition that's true.
name = "Joe"
if name == "Fred":
    print("Hello Fred")
elif name == "Xander":
    print("Hello Xander")
elif name == "Joe":
    print("Hello Joe")
elif name == "Arnold":
    print("Hello Arnold")
else:
    print("I don't know who you are!")

# A more Pythonic alternative using dict.get().
names = {
    "Fred": "Hello Fred",
    "Xander": "Hello Xander",
    "Joe": "Hello Joe",
    "Arnold": "Hello Arnold",
}
print(names.get("Joe", "I don't know who you are!"))
print(names.get("Rick", "I don't know who you are!"))

# Short-circuit evaluation: once a condition is true, the remaining ones
# aren't tested, so neither the division by zero nor the undefined name
# var raises an error.
if "a" in "bar":
    print("foo")
elif 1 / 0:
    print("This won't happen")
elif var:  # noqa: F821
    print("This won't either")
