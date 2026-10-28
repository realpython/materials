import httpx2

with httpx2.Client() as client:
    response = client.post(
        "https://httpbin.org/post",
        json={"title": "New issue", "body": "Found a bug"},
    )
    print(response.status_code)
    print(response.json()["json"])
