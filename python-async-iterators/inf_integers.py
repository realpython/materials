import asyncio


async def async_inf_integers(start=0):
    current = start
    while True:
        yield current
        current += 1
        await asyncio.sleep(0.5)


async def main(stop=5):
    generator = async_inf_integers()
    while True:
        number = await anext(generator)
        # Process the number here...
        print(number)
        if number == stop - 1:
            break


asyncio.run(main(20))
