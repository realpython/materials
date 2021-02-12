import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"

# Define the search term you want to use.
query = "moby dick"

# In the query parameters you can define:
# 1. The number of books to return using the `maxResults` parameter.
# 2. The query term to search for using the `q` parameter.
params = {"q": query, "maxResults": 3}

# The response will contain a list of books that match your query.
response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    # In order to fetch the title, published date and description,
    # you first need to fetch the volume.
    volume = book["volumeInfo"]

    # You can fetch these and other attributes from the book using
    # the specific volume
    title = volume["title"]
    published = volume["publishedDate"]
    description = volume["description"]

    print("%s (%s) | %s" % (title, published, description))
