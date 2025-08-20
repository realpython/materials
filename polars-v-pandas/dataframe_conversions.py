import narwhals as nw
import polars as pl
from data_generation import generate_data

polars_df = pl.DataFrame(data_generation(4))
polars_df

pandas_df = polars_df.to_pandas()
type(pandas_df)
pandas_df

polars_df = pl.from_pandas(pandas_df)
type(polars_df)
polars_df


def agnositic_groupby(df):
    return (
        nw.from_native(df)
        .group_by("region")
        .agg(nw.col("sales_income").sum())
        .sort("region")
        .to_native()
    )


agnositic_groupby(pandas_df)

agnositic_groupby(polars_df)
