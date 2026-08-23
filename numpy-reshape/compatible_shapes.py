"""Reshape into compatible shapes by trimming or extending the data."""

import numpy as np

rng = np.random.default_rng(seed=42)
temperatures = rng.normal(18, 1, size=200)

# An incompatible shape raises a ValueError
try:
    temperatures.reshape((3, 7, 8))
except ValueError as error:
    print(f"ValueError: {error}")

days_per_week = 7
readings_per_day = 8
number_of_weeks = len(temperatures) // (days_per_week * readings_per_day)
trimmed_length = number_of_weeks * days_per_week * readings_per_day

# Option 1: trim the data so that it fits a whole number of weeks
temperatures_week = temperatures[:trimmed_length].reshape(
    (number_of_weeks, days_per_week, readings_per_day)
)
print(f"Trimmed shape: {temperatures_week.shape}")

# Option 2: extend the data with np.nan filler values
extended_length = (number_of_weeks + 1) * (days_per_week * readings_per_day)
additional_length = extended_length - len(temperatures)
temperatures_extended = np.append(
    temperatures, np.full(additional_length, np.nan)
)
temperatures_week = temperatures_extended.reshape(
    (number_of_weeks + 1, days_per_week, readings_per_day)
)
print(f"Extended shape: {temperatures_week.shape}")
