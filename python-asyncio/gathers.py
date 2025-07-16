import asyncio
import time


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


async def main():
    task1 = asyncio.create_task(coro([10, 5, 2]))
    task2 = asyncio.create_task(coro([3, 2, 1]))
    print("Start:", time.strftime("%X"))
    result = await asyncio.gather(task1, task2)
    print("End:", time.strftime("%X"))
    print(f"Both tasks done: {all((task1.done(), task2.done()))}")
    return result


result = asyncio.run(main())
print(f"result: {result}")
