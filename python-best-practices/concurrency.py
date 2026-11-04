# Avoid this:
# import asyncio

# import requests

# async def main():
#     await asyncio.gather(
#         fetch_status("https://example.com"),
#         fetch_status("https://python.org"),
#     )

# async def fetch_status(url):
#     response = requests.get(url)  # Blocking I/O task
#     return response.status_code

# asyncio.run(main())


# Favor this:
import asyncio

import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        statuses = await asyncio.gather(
            fetch_status(session, "https://example.com"),
            fetch_status(session, "https://realpython.com"),
        )
    print(statuses)


async def fetch_status(session, url):
    async with session.get(url) as response:  # Non-blocking I/O task
        return response.status


asyncio.run(main())
