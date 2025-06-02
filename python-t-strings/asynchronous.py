import asyncio


async def get_name():
    # Simulate an asynchronous operation
    await asyncio.sleep(1)
    return "Pythonista"


async def greeting_template():
    return t"Hello, {await get_name()}!"


async def main():
    greeting = await greeting_template()
    print(greeting)


asyncio.run(main())
