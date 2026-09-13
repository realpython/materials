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
    urls = [
        "https://www.google.com",
        "https://www.linkedin.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.facebook.com",
        "https://x.com",
    ]

    work_queue = queue.Queue()
    for url in urls:
        work_queue.put(url)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    with Timer(text="\nTotal elapsed time: {:.1f}"):
        while tasks:
            for current_task in tasks.copy():
                try:
                    next(current_task)
                except StopIteration:
                    tasks.remove(current_task)


if __name__ == "__main__":
    main()
