import asyncio

import httpx2


async def main():
    async with httpx2.AsyncClient() as client:
        async with client.stream(
            "GET", "https://httpbin.org/stream-bytes/102400"
        ) as response:
            async for chunk in response.aiter_bytes(chunk_size=1024):
                print(f"Received {len(chunk)} bytes")


asyncio.run(main())
