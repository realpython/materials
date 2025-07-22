import asyncio


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


async def main():
    task = asyncio.create_task(coro([3, 2, 1]))
    print(f"{type(task) = }")
    print(f"{task.done() = }")
    return await task


result = asyncio.run(main())
print(f"result: {result}")
