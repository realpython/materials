"""Use -1 as a wildcard dimension in reshape()."""

import numpy as np

rng = np.random.default_rng(seed=42)
temperatures = rng.normal(18, 1, size=200)

# Let reshape() infer the first dimension's length with -1
temperatures_day = temperatures.reshape((-1, 8))
print(f"Inferred shape: {temperatures_day.shape}")

# Use -1 to flatten an array of any shape into a single dimension
numbers = rng.integers(1, 100, (2, 4, 3, 3))
print(f"Original shape: {numbers.shape}")
numbers_flattened = numbers.reshape(-1)
print(f"Flattened shape: {numbers_flattened.shape}")
