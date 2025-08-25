import pandas as pd

pd.set_option("display.max_columns", None)

sales_data = pd.read_csv(
    "sales_data_with_missing_values.csv",
    parse_dates=["order_date"],
    date_format="%d/%m/%Y",
).convert_dtypes(dtype_backend="pyarrow")


sales_data.dropna(axis=0, subset=(["discount", "sale_price"]))

sales_data.dropna(how="all")

sales_data.dropna(thresh=5)

sales_data.dropna(thresh=5, ignore_index=True)
