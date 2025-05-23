import asyncio


async def fetch_data():
    print("Fetching data from the server...")
    await asyncio.sleep(1)  # Simulate network delay
    print("Data received!")
    return {"user": "john", "status": "active"}


async def main():
    data = await fetch_data()
    print(f"Received data: {data}")


asyncio.run(main())
