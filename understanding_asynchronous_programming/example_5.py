"""
example_5.py

Just a short example demonstrating a simple state machine in Python
This version is doing actual work, downloading the contents of
URL's it gets from a queue
"""

import asyncio
import urllib.request
from lib.elapsed_time import ET


async def task(name, work_queue):
    while not work_queue.empty():
        url = await work_queue.get()
        print(f"Task {name} getting URL: {url}")
        et = ET()
        response = urllib.request.urlopen(url)
        html = response.read()
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
        "http://shutterfly.com",
        "http://mypublisher.com",
        "http://facebook.com",
    ]:
        await work_queue.put(url)

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
