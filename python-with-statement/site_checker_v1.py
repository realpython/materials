import asyncio

import aiohttp


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"{url}: type -> {html[:17].strip()}")


async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com/"),
    )


asyncio.run(main())
