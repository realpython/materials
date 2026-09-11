# %%
from pathlib import Path

import pandas as pd

project_root = Path.cwd()
if not (project_root / "data").is_dir():
    project_root = project_root.parent
sales = pd.read_csv(project_root / "data/sales_data.csv")
print(sales.shape)
print(sales.head())

# %%
print("Missing cells:", sales.isna().sum().sum())
print("Duplicate rows:", sales.duplicated().sum())
print("Repeated order numbers:", sales["order_number"].duplicated().sum())
print(sales.dtypes)

# %%
columns = ["order_type", "quantity", "unit_price", "sale_price"]
print(sales.nlargest(5, "sale_price")[columns].to_string(index=False))

# %%
clean_sales = sales.rename(columns={"produce_name": "product_name"}).copy()
clean_sales["order_date"] = pd.to_datetime(
    clean_sales["order_date"], format="%d/%m/%Y"
)
clean_sales["product_category"] = (
    clean_sales["product_category"].str.strip().str.title()
)

# %%
expected_total = clean_sales["quantity"] * clean_sales["unit_price"]
mismatches = (clean_sales["sale_price"] - expected_total).abs() > 0.01
print("Inconsistent totals:", mismatches.sum())
clean_sales.to_csv(project_root / "data/sales_clean.csv", index=False)
