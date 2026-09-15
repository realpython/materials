import asyncio

import httpx2


async def main():
    async with httpx2.AsyncClient(base_url="https://api.github.com") as client:
        response = await client.get("/events")
        print(response.status_code)


asyncio.run(main())
