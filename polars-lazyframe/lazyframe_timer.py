import time

import polars as pl

start = time.perf_counter()

for _ in range(10):
    rides = pl.scan_parquet("rides.parquet")
    result = (
        rides.filter(pl.col("pick_up") == pl.col("drop_off"))
        .group_by(pl.col("pick_up"))
        .agg(pl.col("fare").mean())
        .filter(
            pl.col("pick_up").is_in(
                ["Brooklyn", "Bronx", "Queens", "Manhattan"]
            )
        )
    ).collect()

end = time.perf_counter()

f"Code finished in {(end - start)/10:0.4f} seconds."
