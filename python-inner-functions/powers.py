# def generate_power(exponent):
#     def power(base):
#         return base**exponent

#     return power


def generate_power(exponent):
    def power(func):
        def inner_power(*args):
            base = func(*args)
            return base**exponent

        return inner_power

    return power


@generate_power(2)
def square(n):
    return n


print(square(7))


@generate_power(3)
def cube(n):
    return n


print(cube(5))
