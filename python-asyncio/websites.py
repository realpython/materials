import asyncio

import aiohttp


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")


async def main():
    websites = [
        "https://realpython.com",
        "https://pycoders.com",
        "https://www.python.org",
    ]
    await asyncio.gather(*(check(url) for url in websites))


asyncio.run(main())
