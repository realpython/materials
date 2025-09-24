"""
Unpacking operator demo to support the *args discussion.
"""

some_items = ["Coffee", "Tea", "Cake", "Bread"]

print("Passing the list as a single argument:")
print(some_items)  # -> ['Coffee', 'Tea', 'Cake', 'Bread']

print("\nUnpacking the list with *some_items:")
print(*some_items)  # -> Coffee Tea Cake Bread
