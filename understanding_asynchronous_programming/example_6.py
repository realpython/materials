import asyncio
import aiohttp
from lib.elapsed_time import ET


async def task(name, work_queue):
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            et = ET()
            async with session.get(url) as response:
                await response.text()
            print(f"Task {name} total elapsed time: {et():.1f}")


async def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = asyncio.Queue()

    # put some 'work' in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        await work_queue.put(url)

    # run the tasks
    et = ET()
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )
    print(f"\nTotal elapsed time: {et():.1f}")


if __name__ == "__main__":
    asyncio.run(main())
