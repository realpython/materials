import asyncio
import csv

import aiofiles


class AsyncCSVIterator:
    def __init__(self, path):
        self.path = path
        self.file = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.file is None:
            self.file = await aiofiles.open(self.path, mode="r")
            lines = await self.file.readlines()
            self.reader = csv.reader(lines)
        try:
            return next(self.reader)
        except StopIteration:
            await self.file.close()
            raise StopAsyncIteration


async def main():
    csv_iter = AsyncCSVIterator("data.csv")
    # Skip the headers
    await anext(csv_iter)
    # Process the rest of the rows
    async for row in csv_iter:
        print(row)


asyncio.run(main())
