"""Send a GET request to JSONPlaceholder.

From the "GET" section of the tutorial.
"""

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())

# Beyond the JSON data, you can inspect the response itself.
print(response.status_code)
print(response.headers["Content-Type"])
