"""Increase the number of dimensions of an array with reshape()."""

import numpy as np

rng = np.random.default_rng(seed=42)
temperatures = rng.normal(18, 1, size=200)
print(f"Original shape: {temperatures.shape}")

# 200 readings, eight per day, gives 25 rows of eight columns
temperatures_day = temperatures.reshape((25, 8))
print(f"Reshaped into days, shape: {temperatures_day.shape}")
print("Second day's readings:")
print(temperatures_day[1])
