"""Send a POST request to JSONPlaceholder to create a new to-do.

From the "POST" section of the tutorial.
"""

import json

import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())

print(response.status_code)

# An equivalent version that serializes the JSON and sets the
# Content-Type header manually instead of using the json argument.
headers = {"Content-Type": "application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response.json())

print(response.status_code)
