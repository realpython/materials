import asyncio

import httpx2


async def main():
    timeout = httpx2.Timeout(5.0)
    async with httpx2.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.get("https://api.github.com/nonexistent")
            response.raise_for_status()
        except httpx2.ConnectTimeout:
            print("Timed out while connecting to the host.")
        except httpx2.ReadTimeout:
            print("Timed out while receiving data from the host.")
        except httpx2.WriteTimeout:
            print("Timed out while sending data to the host.")
        except httpx2.PoolTimeout:
            print("Timed out waiting for a pool connection.")
        except httpx2.HTTPStatusError as error:
            print(f"Bad response: {error.response.status_code}")
        except httpx2.RequestError as error:
            print(f"A network problem occurred: {error}")


asyncio.run(main())
