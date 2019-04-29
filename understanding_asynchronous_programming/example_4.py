import asyncio
from lib.elapsed_time import ET


async def task(name, work_queue):
    while not work_queue.empty():
        delay = await work_queue.get()
        et = ET()
        print(f"Task {name} running")
        await asyncio.sleep(delay)
        print(f"Task {name} total elapsed time: {et():.1f}")


async def main():
    """
    This is the main entry point for the programWhen
    """
    # create the queue of 'work'
    work_queue = asyncio.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        await work_queue.put(work)

    # run the tasks
    et = ET()
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )
    print(f"\nTotal elapsed time: {et():.1f}")


if __name__ == "__main__":
    asyncio.run(main())
