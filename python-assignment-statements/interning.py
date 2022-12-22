import sys

interning = [x for x, y in zip(range(-10, 500), range(-10, 500)) if x is y]

print(
    f"Interning interval for Python {sys.version[0:6]} is:"
    f" ({interning[0]} to {interning[-1]})"
)
