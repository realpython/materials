import requests

response = requests.get("https://api.github.com/events")
print(response.status_code)
print(response.json())
