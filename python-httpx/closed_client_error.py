import httpx2

with httpx2.Client() as client:
    pass

client.get("https://api.github.com/events")
