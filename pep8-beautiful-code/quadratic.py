def quadratic(a, b, c):
    """Solve quadratic equation via the quadratic formula.

    A quadratic equation has the following form:
    ax**2 + bx + c = 0

    There always two solutions to a quadratic equation: x_1 & x_2.
    """
    x_1 = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x_2 = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)

    return x_1, x_2
