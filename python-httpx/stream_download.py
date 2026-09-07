import httpx2

with httpx2.Client() as client:
    with client.stream(
        "GET", "https://httpbin.org/stream-bytes/102400"
    ) as response:
        print(response.headers)
        for chunk in response.iter_bytes(chunk_size=1024):
            print(f"Received {len(chunk)} bytes")
