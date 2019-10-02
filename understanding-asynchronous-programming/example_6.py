import asyncio
import aiohttp
from codetiming import Timer


async def task(name, work_queue):
    text = ''.join([f'Task {name} elapsed time: ', '{:.2f}'])
    timer = Timer(text=text)
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()


async def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of 'work'
    work_queue = asyncio.Queue()

    # Put some 'work' in the queue
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

    # Run the tasks
    with Timer(text='\nTotal elapsed time: {:.2f}'):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue))
        )


if __name__ == "__main__":
    asyncio.run(main())
