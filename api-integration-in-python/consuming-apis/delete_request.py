"""Send a DELETE request to JSONPlaceholder to remove a to-do.

From the "DELETE" section of the tutorial.
"""

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())

print(response.status_code)
