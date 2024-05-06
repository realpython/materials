import fastparquet
import pandas as pd
import pyarrow.parquet as pq


def main():
    users_df = pd.read_csv("users.csv")
    serialize_with_pandas(users_df, "users.parquet")

    df1 = deserialize_with_pandas("users.parquet")
    df2 = deserialize_with_pyarrow("users.parquet")
    df3 = deserialize_with_fastparquet("users.parquet")

    print(f"{df1.equals(df2) = }")
    print(f"{df2.equals(df3) = }")

    df = prune_and_filter("users.parquet")
    print(df.head())


def serialize_with_pandas(df, filename):
    df.to_parquet(filename)


def deserialize_with_pandas(filename):
    return pd.read_parquet(filename)


def deserialize_with_pyarrow(filename):
    return pq.read_table(filename).to_pandas()


def deserialize_with_fastparquet(filename):
    return fastparquet.ParquetFile(filename).to_pandas()


def prune_and_filter(filename):
    return pd.read_parquet(
        filename,
        filters=[("language", "=", "fr")],
        columns=["id", "name"],
    )


if __name__ == "__main__":
    main()
