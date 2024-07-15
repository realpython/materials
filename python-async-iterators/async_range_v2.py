import asyncio


class AsyncRange:
    def __init__(self, start, end):
        self.data = range(start, end)

    async def __aiter__(self):
        for i in self.data:
            await asyncio.sleep(0.5)
            yield i


async def main():
    async for i in AsyncRange(0, 5):
        print(i)


asyncio.run(main())
