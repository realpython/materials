# %% Different ways to take a sum of a column

import pandas as pd

# %%

websites = pd.read_csv("resources/popular_websites.csv", index_col=0)

# %% Best way: use the dedicated pandas method

websites["total_views"].sum()

# %% List comprehension

sum(website.total_views for website in websites.itertuples())

# %% itertuples()

total = 0
for website in websites.itertuples():
    total += website.total_views

total

# %%
