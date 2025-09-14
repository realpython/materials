import narwhals as nw
import polars as pl
from data_generation import generate_data


def universal_groupby(df):
    return (
        nw.from_native(df)
        .group_by("region")
        .agg(nw.col("sales_income").sum())
        .sort("region")
        .to_native()
    )


if __name__ == "__main__":
    polars_df = pl.DataFrame(generate_data(4))
    print(polars_df)

    pandas_df = polars_df.to_pandas()
    print(type(pandas_df))
    print(pandas_df)

    polars_df = pl.from_pandas(pandas_df)
    print(type(polars_df))
    print(polars_df)

    print(universal_groupby(pandas_df))
    print(universal_groupby(polars_df))
