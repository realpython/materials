import httpx2

with httpx2.Client(http2=True) as client:
    response = client.get("https://api.github.com/events")
    print(response.http_version)
