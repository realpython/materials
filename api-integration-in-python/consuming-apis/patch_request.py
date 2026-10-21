"""Send a PATCH request to JSONPlaceholder to modify one field.

From the "PATCH" section of the tutorial.
"""

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json())

print(response.status_code)
