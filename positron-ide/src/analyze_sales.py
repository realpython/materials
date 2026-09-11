# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

project_root = Path.cwd()
if not (project_root / "data").is_dir():
    project_root = project_root.parent
sales = pd.read_csv(
    project_root / "data/sales_clean.csv", parse_dates=["order_date"]
)

# %%
print(sales[["quantity", "unit_price", "sale_price"]].describe().round(2))
print(sales["order_type"].value_counts())

# %%
order_summary = sales.groupby(
    ["product_category", "order_type"], as_index=False
).agg(
    orders=("order_number", "size"),
    median_order_value=("sale_price", "median"),
    median_quantity=("quantity", "median"),
    median_unit_price=("unit_price", "median"),
)
print(order_summary.round(2).to_string(index=False))

# %%
chart_data = order_summary.pivot(
    index="product_category", columns="order_type", values="median_order_value"
)
ax = chart_data.plot.bar(rot=0, figsize=(8, 4))
ax.set(xlabel="Product category", ylabel="Median order value")
ax.set_title("Retail and Wholesale Order Values")
plt.tight_layout()
plt.show()
