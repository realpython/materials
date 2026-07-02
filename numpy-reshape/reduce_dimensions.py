"""Reduce the number of dimensions of an array with reshape()."""

import numpy as np

rng = np.random.default_rng(seed=42)
results = rng.integers(0, 100, size=(5, 10))

# Pass a one-element tuple to reshape the 2D array into a 1D array
year_results = results.reshape((50,))
print(f"Shape: {year_results.shape}, dimensions: {year_results.ndim}")
print(f"First score: {year_results[0]}")

# Passing a single integer gives the same 1D result
same_results = results.reshape(50)
print(f"Integer argument gives the same shape: {same_results.shape}")
