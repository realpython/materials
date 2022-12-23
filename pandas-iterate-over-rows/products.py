# %%

import pandas as pd

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

# %% The equivalent way to do that with only .itertuples()

products = pd.read_csv("resources/products.csv")

cumulative_sum = []

for row in products.itertuples():
    if cumulative_sum:
        cumulative_sum.append(
            cumulative_sum[-1] + (row.sales * row.unit_price)
        )
    else:
        cumulative_sum.append(row.sales * row.unit_price)

products.assign(cumulative_income=cumulative_sum)
# %%
