import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
params = {"q": "moby dick", "maxResults": 3}

response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume["publishedDate"]
    description = volume["description"]

    print("%s (%s) | %s" % (title, published, description))
