import numpy as np
import polars as pl

num_rows = 5000
rng = np.random.default_rng(seed=7)

buildings_data = {
    "sqft": rng.exponential(scale=1000, size=num_rows),
    "year": rng.integers(low=1995, high=2023, size=num_rows),
    "building_type": rng.choice(["A", "B", "C"], size=num_rows),
}

buildings = pl.DataFrame(buildings_data)
print(buildings)

print(buildings.schema)

print(buildings.head())

print(buildings.describe())
