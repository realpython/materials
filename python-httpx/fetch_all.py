import asyncio

import httpx2


async def fetch_all(paths):
    async with httpx2.AsyncClient(base_url="https://api.github.com") as client:
        coroutines = [client.get(path) for path in paths]
        responses = await asyncio.gather(*coroutines)
        return [response.status_code for response in responses]


paths = ["/events", "/repos/python/cpython", "/repos/psf/requests"]
print(asyncio.run(fetch_all(paths)))
