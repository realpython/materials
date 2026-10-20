from calculator.simple import SimpleCalculator


def create_add_string(x, y):
    """Returns a string containing an addition expression."""
    return f"{x} + {y}"


my_calculator = SimpleCalculator()
my_calculator.run(create_add_string(2, 2))
print(my_calculator.lcd)
