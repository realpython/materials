"""Inspect the shape and number of dimensions of a NumPy array."""

import numpy as np

numbers = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(numbers)
print(f"Shape: {numbers.shape}")
print(f"Number of dimensions: {numbers.ndim}")
