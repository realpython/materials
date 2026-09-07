import httpx2

timeout = httpx2.Timeout(connect=5.0, read=10.0, write=None, pool=5.0)

with httpx2.Client(timeout=timeout) as client:
    response = client.get("https://api.github.com/events")
    print(response.status_code)
