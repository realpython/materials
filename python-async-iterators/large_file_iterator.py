import asyncio

import aiofiles


class AsyncFileIterator:
    def __init__(self, path, chunk_size=1024):
        self.path = path
        self.chunk_size = chunk_size
        self.file = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.file is None:
            self.file = await aiofiles.open(self.path, mode="rb")
        chunk = await self.file.read(self.chunk_size)
        if not chunk:
            await self.file.close()
            raise StopAsyncIteration
        return chunk


async def main():
    async for chunk in AsyncFileIterator("large-file.md"):
        # Process the file chunk here...
        await asyncio.sleep(0.2)
        print(chunk.decode("utf-8"))


asyncio.run(main())
