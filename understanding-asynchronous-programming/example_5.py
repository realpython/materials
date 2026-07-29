import queue

import requests
from codetiming import Timer


def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    with requests.Session() as session:
        while not work_queue.empty():
            url = work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            session.get(url)
            timer.stop()
            yield


def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for url in [
        "https://www.google.com",
        "https://www.linkedin.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.facebook.com",
        "https://x.com",
    ]:
        work_queue.put(url)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        while tasks:
            for t in tasks.copy():
                try:
                    next(t)
                except StopIteration:
                    tasks.remove(t)


if __name__ == "__main__":
    main()
