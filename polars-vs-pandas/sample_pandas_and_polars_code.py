import pandas as pd
import polars as pl

# Pandas index-based syntax
orders_pandas = pd.read_parquet("online_retail.parquet")

orders_pandas["Total"] = orders_pandas["Quantity"] * orders_pandas["UnitPrice"]

orders_pandas[["InvoiceNo", "Quantity", "UnitPrice", "Total"]][
    orders_pandas["Total"] > 100
].head(3)

# Pandas method chaining syntax
orders_pandas = pd.read_parquet("online_retail.parquet")

(
    orders_pandas.assign(Total=orders_pandas["Quantity"] * orders_pandas["UnitPrice"])
    .filter(["InvoiceNo", "Quantity", "UnitPrice", "Total"])
    .query("Total > 100")
).head(3)

# Polars method chaining syntax
orders_polars = pl.read_parquet("online_retail.parquet")

(
    orders_polars.select(
        pl.col(["InvoiceNo", "Quantity", "UnitPrice"]),
        total=pl.col("Quantity") * pl.col("UnitPrice"),
    ).filter(pl.col("total") > 100)
).head(3)
