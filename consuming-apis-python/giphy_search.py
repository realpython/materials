import requests

# REPLACE the following with the API key you generated.
API_KEY = "REPLACE_DEMO_API_KEY"

endpoint = "https://api.giphy.com/v1/gifs/search"

# Define the search term you want to use.
search_term = "shrug"

# In the query parameters you can define:
# 1. The number of GIFs to return using the `limit` parameter.
# 2. The query term to search for using the `q` parameter.
# 3. The accepted rating of the GIFs returned using the `rating` parameter
# https://developers.giphy.com/docs/optional-settings#rating
params = {"api_key": API_KEY, "limit": 3, "q": search_term, "rating": "g"}

# The response will contain a list with all the GIFs that match your query.
# For each of those, you want to get the `title` and `url` fields.
response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    url = gif["url"]
    print("%s | %s" % (title, url))
