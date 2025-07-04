def power_factory(exponent):
    def power(base):
        return base**exponent

    return power


square = power_factory(2)
print(square(10))

cube = power_factory(3)
print(cube(10))
