import httpx2

response = httpx2.get("https://api.github.com/events")
print(response.status_code)
print(response.json())
