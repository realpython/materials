import asyncio


class AsyncRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start < self.end:
            await asyncio.sleep(0.5)
            value = self.start
            self.start += 1
            return value
        else:
            raise StopAsyncIteration


async def main():
    async for i in AsyncRange(0, 5):
        print(i)


asyncio.run(main())
