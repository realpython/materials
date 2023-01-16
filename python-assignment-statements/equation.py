from math import sqrt

a, b, c = 2.0, -1.0, -4.0

x1, x2 = (
    (-b - sqrt(b**2 - 4 * a * c)) / (2 * a),
    (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
)

print(f"{x1=}, {x2=}")
