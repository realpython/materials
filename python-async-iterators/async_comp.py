import asyncio


async def async_range(start, end):
    for i in range(start, end):
        await asyncio.sleep(0.2)
        yield i


async def main():
    number_list = [i async for i in async_range(0, 5)]
    number_dict = {i: str(i) async for i in async_range(0, 5)}
    print(number_list)
    print(number_dict)


asyncio.run(main())
