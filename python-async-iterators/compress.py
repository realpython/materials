import asyncio
from pathlib import Path

import aiofiles
from zipstream import AioZipStream


async def stream_generator(files):
    async_zipstream = AioZipStream(files)
    async for chunk in async_zipstream.stream():
        yield chunk


async def main(directory, zip_name="output.zip"):
    files = [{"file": path} for path in directory.iterdir() if path.is_file()]
    async with aiofiles.open(zip_name, mode="wb") as archive:
        async for chunk in stream_generator(files):
            await archive.write(chunk)


directory = Path.cwd()
asyncio.run(main(directory))
