from urllib.request import urlopen

url = "https://example.com/"

with urlopen(url) as response:
    raw_bytes: bytes = response.read()

print(f"Bytes: {raw_bytes[:100]}\n")

string_format = raw_bytes[:100].decode()

print(f"String format: {string_format}\n")
