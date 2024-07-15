import asyncio
from pathlib import Path

import aiofiles
from zipstream import AioZipStream


async def stream_generator(files):
    async_zipstream = AioZipStream(files)
    async for chunk in async_zipstream.stream():
        yield chunk


async def main(directory, zip_name="output.zip"):
    files = [{"file": file} for file in directory.iterdir()]

    async with aiofiles.open(zip_name, mode="wb") as z:
        async for chunk in stream_generator(files):
            await z.write(chunk)


directory = Path()
asyncio.run(main(directory))
