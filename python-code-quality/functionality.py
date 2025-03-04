# def add_numbers(a, b):
#     return a + b


def add_numbers(a: int | float, b: int | float) -> int | float:
    a, b = float(a), float(b)
    return a + b


print(add_numbers(2, 3))
print(add_numbers(2, "3"))
