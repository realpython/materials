import asyncio
from random import randint


class AsyncCounterIterator:
    def __init__(self, name="", end=5):
        self.counter = 0
        self.name = name
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= self.end:
            raise StopAsyncIteration
        self.counter += 1
        await asyncio.sleep(randint(1, 3) / 10)
        return self.counter


async def task(iterator):
    async for item in iterator:
        print(item, f"from iterator {iterator.name}")


async def main():
    # This code runs sequentially:
    # await task(AsyncCounterIterator("#1"))
    # await task(AsyncCounterIterator("#2"))

    # This is concurrent:
    await asyncio.gather(
        task(AsyncCounterIterator("#1")),
        task(AsyncCounterIterator("#2")),
    )


asyncio.run(main())
