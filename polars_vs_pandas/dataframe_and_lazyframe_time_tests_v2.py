import sys
import time

import pandas as pd
import polars as pl

from data_generation import data_generation

# Data Generation

test_data = data_generation(int(sys.argv[1]))

# Polars DataFrame Test

polars_dataframe = pl.DataFrame(test_data)

(
    polars_dataframe.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    )
)

# Polars LazyFrame Test

polars_lazyframe = pl.LazyFrame(test_data)

(
    polars_lazyframe.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    )
).collect()


# Pandas DataFrame Test

pandas_dataframe = pd.DataFrame(test_data)

pandas_dataframe.groupby(["region", "product", "sales_person"])[
    "sales_income"
].sum()

# Polars LazyFrame Streaming Test

overall_time_start = time.time()

polars_lazyframe = pl.LazyFrame(test_data)

processing_time_start = time.time()

(
    polars_lazyframe.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    )
).collect(engine="streaming")

end_time = time.time()

print(
    f"Polars Streaming LazyFrame creation: {processing_time_start - overall_time_start}"
)
print(
    f"Polars Streaming LazyFrame query runtime: {end_time - processing_time_start}"
)
print(
    f"Polars Streaming LazyFrame overall time: {end_time - overall_time_start}"
)
print()
