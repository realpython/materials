import pandas as pd
import polars as pl

orders_pandas = pd.read_parquet("Online_Retail.parquet")

orders_pandas["Total"] = orders_pandas["Quantity"] * orders_pandas["UnitPrice"]

orders_pandas[["InvoiceNo", "Quantity", "UnitPrice", "Total"]][
    orders_pandas["Total"] > 10
].head(3)


orders_polars = pl.read_csv("online_retail.csv")

orders_polars = pl.read_parquet("online_retail.parquet")

(
    orders_polars.select(
        pl.col(["InvoiceNo", "Quantity", "UnitPrice"]),
        total=pl.col("Quantity") * pl.col("UnitPrice"),
    ).filter(pl.col("total") > 10)
).head(3)
