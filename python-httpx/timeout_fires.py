import httpx2

timeout = httpx2.Timeout(1.0)

with httpx2.Client(timeout=timeout) as client:
    try:
        client.get("https://httpbin.org/delay/3")
    except httpx2.ReadTimeout:
        print("The request timed out.")
