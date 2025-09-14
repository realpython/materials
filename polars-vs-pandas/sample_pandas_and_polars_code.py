import pandas as pd
import polars as pl


orders_pandas = pd.read_parquet("online_retail.parquet")

orders_pandas["Total"] = (
    orders_pandas["Quantity"] * orders_pandas["UnitPrice"]
)

orders_pandas[["InvoiceNo", "Quantity", "UnitPrice", "Total"]][
    orders_pandas["Total"] > 100
].head(3)


(
    orders_pandas
    .assign(Total=orders_pandas["Quantity"] * orders_pandas["UnitPrice"])
    .filter(["InvoiceNo", "Quantity", "UnitPrice", "Total"])
    .query("Total > 100")
).head(3)


orders_polars = pl.read_parquet("online_retail.parquet")

(
    orders_polars.select(
        pl.col(["InvoiceNo", "Quantity", "UnitPrice"]),
        Total=pl.col("Quantity") * pl.col("UnitPrice"),
    ).filter(pl.col("Total") > 100)
).head(3)

