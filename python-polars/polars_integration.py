import numpy as np
import pandas as pd
import polars as pl

data = pl.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})

data.write_csv("data.csv")
data.write_ndjson("data.json")
data.write_parquet("data.parquet")

data_csv = pl.read_csv("data.csv")
data_csv_lazy = pl.scan_csv("data.csv")
print(data_csv_lazy.schema)

data_json = pl.read_ndjson("data.json")
data_json_lazy = pl.scan_ndjson("data.json")
print(data_json_lazy.schema)

data_parquet = pl.read_parquet("data.parquet")
data_parquet_lazy = pl.scan_parquet("data.parquet")
print(data_parquet_lazy.schema)

polars_data = pl.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})

pandas_data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})

numpy_data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]).T

print(pl.from_pandas(pandas_data))

print(pl.from_numpy(numpy_data, schema={"A": pl.Int64, "B": pl.Int64}))

print(polars_data.to_pandas())

print(polars_data.to_numpy())
