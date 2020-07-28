import requests

# Replace the following with the API key generated above.
api_key = "API_KEY"
endpoint = "https://api.giphy.com/v1/gifs/search"
search_term = "shrug"
params = {"api_key": api_key, "limit": 1, "q": search_term, "rating": "g"}

response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    url = gif["url"]
    print("%s | %s" % (title, url))
