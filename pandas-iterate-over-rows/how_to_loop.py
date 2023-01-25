# %%
import httpx
import pandas as pd

# %% Read CSV and rename headers
websites = pd.read_csv("resources/popular_websites.csv", index_col=0)
print(websites)


# %% Define function to check connection
def check_connection(name, url):
    try:
        response = httpx.get(url)
        location = response.headers.get("location")
        if location is None or location.startswith(url):
            print(f"{name} is online!")
        else:
            print(f"{name} is online! But redirects to {location}")
        return True
    except httpx.ConnectError:
        print(f"Failed to establish a connection with {url}")
        return False


# %% Use .itertuples() to iterate through all rows
for website in websites.itertuples():
    check_connection(website.name, website.url)

# %% You may use .iterrows() if you have dynamic columnnames
name_column = "name"
url_column = "url"
for _, website in websites.iterrows():
    check_connection(website[name_column], website[url_column])

# %% Use list comprehension to iterate through all rows
#    Note that this creates a list that is thrown away again
[
    check_connection(website.name, website.url)
    for website in websites.itertuples()
]

# %% Use the index to iterate through rows
for i in websites.index:
    print({**websites.iloc[i]})

# %% Transpose and cast to dictionary to iterate through rows
for website in websites.T.to_dict().values():
    print(website)

# %% Use .agg() to aggregate over columns
websites.agg(
    total_views=("total_views", "sum"),
    average_views=("total_views", "mean"),
)
