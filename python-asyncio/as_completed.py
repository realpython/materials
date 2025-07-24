import asyncio
import time


async def main():
    task1 = asyncio.create_task(coro([10, 5, 2]))
    task2 = asyncio.create_task(coro([3, 2, 1]))
    print("Start:", time.strftime("%X"))
    for task in asyncio.as_completed([task1, task2]):
        result = await task
        print(f'result: {result} completed at {time.strftime("%X")}')
    print("End:", time.strftime("%X"))
    print(f"Both tasks done: {all((task1.done(), task2.done()))}")


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


if __name__ == "__main__":
    asyncio.run(main())
