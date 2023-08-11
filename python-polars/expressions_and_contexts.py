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

print(buildings.select("sqft"))

print(buildings.select(pl.col("sqft")))

print(buildings.select(pl.col("sqft").sort() / 1000))

after_2015 = buildings.filter(pl.col("year") > 2015)
print(after_2015.shape)
print(after_2015.select(pl.col("year").min()))

print(
    buildings.groupby("building_type").agg(
        [
            pl.mean("sqft").alias("mean_sqft"),
            pl.median("year").alias("median_year"),
            pl.count(),
        ]
    )
)
