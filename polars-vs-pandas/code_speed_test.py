import sys
import time

import pandas as pd
import polars as pl
from data_generation import data_generation

# Create DataFrames

data_source = data_generation(int(sys.argv[1]))

orders_pandas = pd.DataFrame(data_source).convert_dtypes(
    dtype_backend="pyarrow"
)

orders_polars = pl.DataFrame(data_source)

# pandas DataFrame Test

start_time = time.time()

orders_pandas.groupby("region")["sales_income"].sum()

end_time = time.time()

print(f"pandas Time Taken: {end_time-start_time}.")

# Polars DataFrame Test

start_time = time.time()

(
    orders_polars.group_by("region").agg(
        total=pl.col("sales_income").sum(),
    )
)

end_time = time.time()

# Results

print(f"polars Time Taken: {end_time-start_time}.")

print(f"----- For {sys.argv[1]} rows")
