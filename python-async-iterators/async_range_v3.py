import asyncio


async def async_range(start, end):
    for i in range(start, end):
        await asyncio.sleep(0.5)
        yield i


async def main():
    async for i in async_range(0, 5):
        print(i)


asyncio.run(main())
