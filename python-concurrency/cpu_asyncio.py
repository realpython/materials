import asyncio
import time


async def main():
    start_time = time.perf_counter()
    tasks = [fib(35) for _ in range(20)]
    await asyncio.gather(*tasks, return_exceptions=True)
    duration = time.perf_counter() - start_time
    print(f"Computed in {duration} seconds")


async def fib(n):
    return n if n < 2 else await fib(n - 2) + await fib(n - 1)


if __name__ == "__main__":
    asyncio.run(main())
