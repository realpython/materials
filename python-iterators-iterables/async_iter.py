import asyncio
from random import randint


class AsyncIterable:
    def __init__(self, stop):
        self.stop = stop
        self.index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.index >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(value := randint(1, 3))
        self.index += 1
        return value


async def main():
    async for num in AsyncIterable(4):
        print(num)


asyncio.run(main())
