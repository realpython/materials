import functools
import sys
from timeit import Timer

import polars as pl

from data_generation import data_generation


def create_polars_lazyframe(test_data):
    return pl.LazyFrame(test_data)


def analyze_polars_lazyframe(polars_lf):
    polars_lf.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    ).collect()


def analyze_polars_streaming(polars_lf):
    polars_lf.group_by(["region", "product", "sales_person"]).agg(
        total_sales=pl.col("sales_income").sum()
    ).collect(engine="streaming")


test_data = data_generation(int(sys.argv[1]))

polars_lf = create_polars_lazyframe(test_data)

print()
print(f"Polars lazyframe analysis time for {int(sys.argv[1])} rows:")
print(Timer(functools.partial(analyze_polars_lazyframe, polars_lf)).timeit(100))

print(f"Polars streaming analysis time for {int(sys.argv[1])} rows:")
print(Timer(functools.partial(analyze_polars_streaming, polars_lf)).timeit(100))
