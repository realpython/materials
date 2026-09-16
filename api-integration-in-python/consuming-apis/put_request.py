"""Send a PUT request to JSONPlaceholder to replace an existing to-do.

From the "PUT" section of the tutorial.
"""

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())

print(response.status_code)
