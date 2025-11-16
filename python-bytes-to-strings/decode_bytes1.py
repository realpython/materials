from urllib.request import urlopen

url = "https://example.com/"

with urlopen(url) as response:
    raw_bytes: bytes = response.read()

print("Bytes:", raw_bytes[:100])
