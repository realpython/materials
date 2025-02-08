import asyncio


class AsyncRange:
    def __init__(self, start, end):
        self.data = range(start, end)

    async def __aiter__(self):
        for index in self.data:
            await asyncio.sleep(0.5)
            yield index


async def main():
    async for index in AsyncRange(0, 5):
        print(index)


asyncio.run(main())
