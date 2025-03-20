from fractions import Fraction

cf = [1]
cf.append(cf)


def evaluate(depth):
    if depth > 0:
        return cf[0] + Fraction(1, evaluate(depth - 1))
    return cf[0]


golden_ratio = (1 + 5**0.5) / 2
for n in range(21):
    fraction = evaluate(n)
    approximation = float(fraction)
    error = abs(golden_ratio - approximation)
    print(
        f"n={n:<3}",
        f"{fraction:>11}",
        "\N{ALMOST EQUAL TO}",
        f"{approximation:.15f}",
        f"(\N{GREEK CAPITAL LETTER DELTA} = {error:<11.10f})",
    )
