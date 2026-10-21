import httpx2

timeout = httpx2.Timeout(5.0, read=15.0)

with httpx2.Client(timeout=timeout) as client:
    response = client.get("https://httpbin.org/delay/6")
    print(response.status_code)
