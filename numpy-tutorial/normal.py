"""Validating the Normal Distribution."""

from numpy.random import default_rng


rng = default_rng()
values = rng.standard_normal(10000)

print(values[:5])
# => array([.9779210858, 1.8361585253, -.3641365235, -.1311344527,
#          1.286542056 ])

std = values.std()
filtered = values[(values > -2 * std) & (values < 2 * std)]

print(filtered.size)
# => 9565
print(values.size)
# => 10000
print(filtered.size / values.size)
# => 0.9565 (actual is .9545)
