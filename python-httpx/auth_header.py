import httpx2

with httpx2.Client(
    base_url="https://api.github.com",
    headers={
        "Authorization": "Bearer your-token",
        "Accept": "application/vnd.github+json",
    },
) as client:
    first = client.get("/events")
    second = client.get("/repos/python/cpython")

print(first.status_code, second.status_code)
print(second.request.headers["Accept"])
