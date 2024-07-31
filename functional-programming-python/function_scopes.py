"""
Example of a nested function scope.
"""


def outer():
    def inner():
        print("I am function inner()!")

    # Function outer() returns function inner().
    return inner


function = outer()

print(function)
print(function())
print(outer()())
