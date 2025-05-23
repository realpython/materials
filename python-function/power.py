def generate_power(exponent):
    def power(base):
        return base**exponent

    return power


square = generate_power(2)
print(square(4))
print(square(6))

cube = generate_power(3)
print(cube(3))
print(cube(5))
