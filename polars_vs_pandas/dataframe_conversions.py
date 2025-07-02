import narwhals as nw
import pandas as pd
import polars as pl

polars_df = pl.DataFrame(
    {
        "a": ["a", "b", "a", "b", "c"],
        "b": [1, 2, 1, 3, 3],
        "c": [5, 4, 3, 2, 1],
    }
)

pandas_df = polars_df.to_pandas()
type(pandas_df)

polars_df = pl.from_pandas(pandas_df)
type(polars_df)


def agnositic_groupby(df):
    return (
        nw.from_native(df)
        .group_by("a")
        .agg(nw.col("b").sum())
        .sort("a")
        .to_native()
    )


agnositic_groupby(pandas_df)

agnositic_groupby(polars_df)
