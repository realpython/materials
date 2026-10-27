import asyncio

import httpx2


async def main():
    timeout = httpx2.Timeout(1.0)
    async with httpx2.AsyncClient(timeout=timeout) as client:
        try:
            await client.get("https://httpbin.org/delay/3")
        except httpx2.TimeoutException:
            print("The request timed out.")


asyncio.run(main())
