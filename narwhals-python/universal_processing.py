import narwhals as nw
from narwhals.typing import FrameT, IntoFrameT


def universal_groupby_v1(df: IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df)
        .group_by("party_name")
        .agg(nw.col("last_name").count())
        .sort("party_name")
        .to_native()
    )


@nw.narwhalify
def universal_groupby_v2(df: FrameT) -> FrameT:
    return (
        df.group_by("party_name")
        .agg(nw.col("last_name").count())
        .sort("party_name")
    )


def universal_groupby_v3(df: IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df)
        .group_by("party_name")
        .agg(nw.col("last_name").count())
        .sort("party_name")
        .to_polars()
    )


def universal_pivot_v1(df: IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df)
        .pivot(
            on="party_name",
            index="century",
            values="last_name",
            aggregate_function="count",
        )
        .to_native()
    )


def universal_pivot_v2(df: IntoFrameT) -> IntoFrameT:
    if isinstance(nw.from_native(df), nw.LazyFrame):
        df = nw.from_native(df).collect()
    return (
        nw.from_native(df)
        .pivot(
            on="party_name",
            index="century",
            values="last_name",
            aggregate_function="count",
        )
        .to_native()
    )
