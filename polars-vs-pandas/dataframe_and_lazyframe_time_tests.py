import sys
import time

import pandas as pd
import polars as pl
from data_generation import data_generation

# Data Generation

test_data = data_generation(int(sys.argv[1]))

# Polars DataFrame Test

overall_time_start = time.time()

polars_dataframe = pl.DataFrame(test_data)

processing_time_start = time.time()

(
    polars_dataframe.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    )
)

end_time = time.time()

del polars_dataframe

print(
    f"Polars DataFrame creation: {processing_time_start - overall_time_start}"
)
print(f"Polars DataFrame query runtime: {end_time - processing_time_start}")
print(f"Polars DataFrame overall time: {end_time - overall_time_start}")
print()

# Polars LazyFrame Test

overall_time_start = time.time()

polars_lazyframe = pl.LazyFrame(test_data)

processing_time_start = time.time()

(
    polars_lazyframe.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    )
).collect()

end_time = time.time()

del polars_lazyframe

print(
    f"Polars LazyFrame creation: {processing_time_start - overall_time_start}"
)
print(f"Polars LazyFrame query runtime: {end_time - processing_time_start}")
print(f"Polars LazyFrame overall time: {end_time - overall_time_start}")
print()

# Pandas DataFrame Test

overall_time_start = time.time()

pandas_dataframe = pd.DataFrame(test_data)

processing_time_start = time.time()

pandas_dataframe.groupby(["region", "product", "sales_person"])[
    "sales_income"
].sum()

end_time = time.time()

del pandas_dataframe

print(
    f"Pandas DataFrame creation: {processing_time_start - overall_time_start}"
)
print(f"Pandas DataFrame query runtime: {end_time - processing_time_start}")
print(f"Pandas DataFrame overall time: {end_time - overall_time_start}")
