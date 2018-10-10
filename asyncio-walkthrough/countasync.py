#!/usr/bin/env python3
# countasync.py

import asyncio


async def us():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(us(), us(), us())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
