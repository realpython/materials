import pandas as pd

pd.set_option("display.max_columns", None)

sales_data = pd.read_csv(
    "sales_data_with_missing_values.csv",
    parse_dates=["order_date"],
    date_format="%d/%m/%Y",
).convert_dtypes(dtype_backend="pyarrow")

print(sales_data)
print(sales_data.isna().sum())
print(sales_data.dropna())

clean_sales_data = sales_data.dropna()
print(clean_sales_data)

sales_data.dropna(inplace=True)
print(sales_data)
