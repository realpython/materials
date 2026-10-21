age = 20

is_adult = age > 18
print(is_adult)

print(type(is_adult))

number = 42

validation_conditions = (
    isinstance(number, int),
    number % 2 == 0,
)

print(all(validation_conditions))

print(callable(number))
print(callable(print))

# The and operator with Boolean operands
print(5 < 7 and 3 == 3)
print(5 < 7 and 3 != 3)
print(5 > 7 and 3 == 3)
print(5 > 7 and 3 != 3)

# The or operator with Boolean operands
print(5 < 7 or 3 == 3)
print(5 < 7 or 3 != 3)
print(5 > 7 or 3 == 3)
print(5 > 7 or 3 != 3)

# The not operator with a Boolean operand
print(5 < 7)
print(not 5 < 7)
