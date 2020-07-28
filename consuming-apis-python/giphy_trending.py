import requests

# Replace the following with the API key generated.
api_key = "API_KEY"
endpoint = "https://api.giphy.com/v1/gifs/trending"
params = {"api_key": api_key, "limit": 3, "rating": "g"}

response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print("%s | %s | %s" % (title, trending_date, url))
