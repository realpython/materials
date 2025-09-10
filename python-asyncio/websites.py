import asyncio

import aiohttp


async def main():
    websites = [
        "https://realpython.com",
        "https://pycoders.com",
        "https://www.python.org",
    ]
    await asyncio.gather(*(check(url) for url in websites))


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")


if __name__ == "__main__":
    asyncio.run(main())
