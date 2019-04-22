"""
example_4.py

Just a short example demonstrating a simple state machine in Python
However, this one has delays that affect it
"""

import asyncio
import queue
from lib.elapsed_time import ET


async def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        et = ET()
        for x in range(count):
            print(f"Task {name} running")
            await asyncio.sleep(1)
            total += 1
        print(f"Task {name} total: {total}")
        print(f"Task {name} total elapsed time: {et():.1f}")


async def main():
    """
    This is the main entry point for the programWhen
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # run the tasks
    et = ET()
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )
    print()
    print(f"Total elapsed time: {et():.1f}")


if __name__ == "__main__":
    asyncio.run(main())
