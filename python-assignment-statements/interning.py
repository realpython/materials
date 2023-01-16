from platform import python_version

interning = [x for x, y in zip(range(-10, 500), range(-10, 500)) if x is y]

print(
    f"Interning interval for Python {python_version()} is:"
    f" ({interning[0]} to {interning[-1]})"
)
