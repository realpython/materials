import functools
import sys
from timeit import Timer

import pandas as pd
import polars as pl

from data_generation import data_generation


def create_pandas_dataframe(test_data):
    return pd.DataFrame(test_data).convert_dtypes(dtype_backend="pyarrow")


def create_polars_dataframe(test_data):
    return pl.DataFrame(test_data)


def create_polars_lazyframe(test_data):
    return pl.LazyFrame(test_data)


def analyze_pandas_dataframe(pandas_df):
    pandas_df.groupby(["region", "product", "sales_person"])[
        "sales_income"
    ].sum()


def analyze_polars_dataframe(polars_df):
    polars_df.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    )


def analyze_polars_lazyframe(polars_lf):
    polars_lf.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    ).collect()


test_data = data_generation(int(sys.argv[1]))

print(f"Pandas dataframe creation time for {int(sys.argv[1])} rows:")
print(Timer(functools.partial(create_pandas_dataframe, test_data)).timeit(100))
print()
print(f"Polars dataframe creation time for {int(sys.argv[1])} rows:")
print(Timer(functools.partial(create_polars_dataframe, test_data)).timeit(100))
print()
print(f"Polars lazyframe creation time for {int(sys.argv[1])} rows:")
print(Timer(functools.partial(create_polars_lazyframe, test_data)).timeit(100))

print()

pandas_df = create_pandas_dataframe(test_data)
polars_df = create_polars_dataframe(test_data)
polars_lf = create_polars_lazyframe(test_data)

print(f"Pandas dataframe analysis time for {int(sys.argv[1])} rows:")
print(
    Timer(functools.partial(analyze_pandas_dataframe, pandas_df)).timeit(100)
)

print()
print(f"Polars dataframe analysis time for {int(sys.argv[1])} rows:")
print(
    Timer(functools.partial(analyze_polars_dataframe, polars_df)).timeit(100)
)

print()
print(f"Polars lazyframe analysis time for {int(sys.argv[1])} rows:")
print(
    Timer(functools.partial(analyze_polars_lazyframe, polars_lf)).timeit(100)
)
