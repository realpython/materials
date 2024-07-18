import asyncio

import aiofiles


class AsyncFileIterable:
    def __init__(self, path, chunk_size=1024):
        self.path = path
        self.chunk_size = chunk_size

    async def __aiter__(self):
        async with aiofiles.open(self.path, mode="rb") as file:
            while True:
                chunk = await file.read(self.chunk_size)
                if not chunk:
                    break
                yield chunk


async def main():
    async for chunk in AsyncFileIterable("large-file.md"):
        # Process the file chunk here...
        await asyncio.sleep(0.2)
        print(chunk.decode("utf-8"))


asyncio.run(main())
