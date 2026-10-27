import httpx2

with httpx2.Client(base_url="https://api.github.com") as client:
    first = client.get("/events")
    second = client.get(
        "/repos/python/cpython/issues",
        params={"state": "open", "per_page": 5},
    )
print(first.status_code, second.status_code)
