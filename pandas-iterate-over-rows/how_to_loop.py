# %%
import httpx
import pandas as pd

# %% Read CSV and rename headers
webs = pd.read_csv("resources/popular_websites.csv", index_col=0)

# %% Define function to check connection
def check_connection(name, url):
    try:
        httpx.get(url)
    except httpx.ConnectError:
        print("Failed to establish a connection")
        return False
    print(f"{name} is online!")
    return True


# %% Use .itertuples() to iterate through all rows
for web in webs.itertuples():
    check_connection(web.website, web.url)

# %%
for _, web in webs.iterrows():
    check_connection(web["website"], web["url"])

# %% Use list comprehension to iterate through all rows
[check_connection(web.website, web.url) for web in webs.itertuples()]

# %% Use the index to iterate through rows
for i in webs.index:
    print({**webs.iloc[i]})

# %% Transpose and cast to dictionary to iterate through rows
for row in webs.T.to_dict().values():
    print(row)

# %%
webs.aggregate(["sum"])
