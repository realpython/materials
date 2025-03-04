# def divide_numbers(a, b):
#     return a / b


def divide_numbers(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: can't divide by zero")


print(divide_numbers(10, 2))
print(divide_numbers(3, 0))
