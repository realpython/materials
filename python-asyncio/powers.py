import asyncio


async def powers_of_two(stop=10):
    exponent = 0
    while exponent < stop:
        yield 2**exponent
        exponent += 1
        await asyncio.sleep(0.2)  # Simulate some asynchronous work


async def main():
    g = []
    async for i in powers_of_two(5):
        g.append(i)
    print(g)

    f = [j async for j in powers_of_two(5) if not (j // 3 % 5)]
    print(f)


if __name__ == "__main__":
    asyncio.run(main())
