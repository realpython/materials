# %%
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path.cwd()

sales = pd.read_csv(PROJECT_ROOT / "data/sales_data.csv")

print(sales.shape)
print(sales.head())

# %%
print("Missing cells:", sales.isna().sum().sum())
print("Duplicate rows:", sales.duplicated().sum())
print("Repeated order numbers:", sales["order_number"].duplicated().sum())
print(sales.dtypes)

# %%
clean_sales = sales.rename(columns={"produce_name": "product_name"}).copy()
clean_sales["order_date"] = pd.to_datetime(
    clean_sales["order_date"], format="%d/%m/%Y"
)
clean_sales["product_category"] = (
    clean_sales["product_category"].str.strip().str.title()
)

# %%
clean_sales.to_csv(PROJECT_ROOT / "data/sales_clean.csv", index=False)
