numbers: tuple[int, ...]

# Allowed:
numbers = (1,)
numbers = (4, 5, 6, 99)


# Not allowed:
numbers = (1, "a")
numbers = [1, 3]
