from math import isclose

x = 1.1 + 2.2

print(x == 3.3)
print(1.1 + 2.2)

# Compare floating-point values for approximate equality instead
print(isclose(x, 3.3))
