import asyncio

import aiohttp
from codetiming import Timer


async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            async with asyncio.timeout(10):
                async with session.get(url) as response:
                    await response.text()
            timer.stop()


async def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    for url in [
        "https://www.google.com",
        "https://www.linkedin.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.facebook.com",
        "https://x.com",
    ]:
        await work_queue.put(url)

    # Run the tasks
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        async with asyncio.TaskGroup() as group:
            group.create_task(task("One", work_queue))
            group.create_task(task("Two", work_queue))


if __name__ == "__main__":
    asyncio.run(main())
