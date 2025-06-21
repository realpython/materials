import pandas as pd

sales_data = pd.read_csv(
    "sales_data_with_missing_values.csv",
    parse_dates=["order_date"],
    date_format="%d/%m/%Y",
).convert_dtypes(dtype_backend="pyarrow")

sales_data

sales_data.isna().sum()

sales_data.dropna()

clean_sales_data = sales_data.dropna()

clean_sales_data = sales_data.dropna(inplace=True)
