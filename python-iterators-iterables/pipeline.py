def to_square(numbers):
    return (number**2 for number in numbers)


def to_cube(numbers):
    return (number**3 for number in numbers)


def to_even(numbers):
    return (number for number in numbers if number % 2 == 0)


def to_odd(numbers):
    return (number for number in numbers if number % 2 != 0)


def to_string(numbers):
    return (str(number) for number in numbers)


print(list(to_string(to_square(to_even(range(20))))))
print(list(to_string(to_cube(to_odd(range(20))))))
