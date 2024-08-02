"""
Examples of using functions as objects.
"""


# Call a function.
def func():
    print("I am function func()!")


func()


# Assign it to a new name.
another_name = func
another_name()

# Show a string representation of a function object.
print("cat", func, 42)

# Access a function object in a list.
objects = ["cat", func, 42]
print(objects[1])

objects[1]()

# Use a function object as a key in a dictionary.
# Note that this is probably not a good idea.
d = {"cat": 1, func: 2, 42: 3}
print(d[func])


# Pass a function as an argument.
def inner():
    print("I am function inner()!")


def outer(function):
    function()


print(outer(inner))
