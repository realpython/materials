import asyncio


async def main():
    greeting = await greeting_template()
    print(greeting)


async def greeting_template():
    """Uncomment in Python 3.14+"""
    # return t"Hello, {await get_name()}!"


async def get_name():
    # Simulate an asynchronous operation
    await asyncio.sleep(0.5)
    return "Pythonista"


asyncio.run(main())
