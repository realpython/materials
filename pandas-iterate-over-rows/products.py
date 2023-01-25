# %%
import pandas as pd

# %% Get the cumulative sum with .itertuples()
products = pd.read_csv("resources/products.csv")

cumulative_sum = []

for product in products.itertuples():
    income = product.sales * product.unit_price
    if cumulative_sum:
        cumulative_sum.append(cumulative_sum[-1] + income)
    else:
        cumulative_sum.append(income)

products = products.assign(cumulative_income=cumulative_sum)

# %% To get cumulative sum, instead of looping, you can create intermediate
# columns and use .cumsum()
products = (
    pd.read_csv("resources/products.csv")
    .assign(
        income=lambda df: df["sales"] * df["unit_price"],
        cumulatative_income=lambda df: df["income"].cumsum(),
    )
    .drop(columns="income")
)
