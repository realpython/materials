"""Change an array's shape with reshape() without changing its data.

The random generator is seeded so that the output is reproducible.
"""

import numpy as np

rng = np.random.default_rng(seed=42)
results = rng.integers(0, 100, size=(5, 10))
print(f"Original results, shape {results.shape}:")
print(results)

# Reshape the five classes of ten scores into a single row
year_results = results.reshape((1, 50))
print(f"\nReshaped to one row, shape {year_results.shape}:")
print(year_results)

# year_results is still 2D, so you index it with both a row and a column
print(f"\nFirst score: {year_results[0, 0]}")
