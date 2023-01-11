# %% Different ways to take a sum of a column

import pandas as pd

# %%

webs = pd.read_csv("resources/popular_websites.csv", index_col=0)

# %% Best way: use the dedicated pandas method

webs["total_views"].sum()

# %% List comprehension

sum(row.total_views for row in webs.itertuples())

# %% itertuples()

total = 0
for row in webs.itertuples():
    total += row.total_views

total

# %%
