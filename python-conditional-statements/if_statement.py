"""The simplest form of the if statement.

Code from the "Introduction to the if Statement" section of the tutorial.
Each condition is marked as truthy or falsy. Only the truthy ones print.
"""

x = 0
y = 5

if x < y:  # Truthy
    print("yes")

if y < x:  # Falsy
    print("yes")

if x:  # Falsy
    print("yes")

if y:  # Truthy
    print("yes")

if x or y:  # Truthy
    print("yes")

if x and y:  # Falsy
    print("yes")

if "aul" in "grault":  # Truthy
    print("yes")

if "quux" in ["foo", "bar", "baz"]:  # Falsy
    print("yes")
