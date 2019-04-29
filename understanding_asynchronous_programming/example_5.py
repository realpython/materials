import queue
import requests
from lib.elapsed_time import ET


def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print(f"Task {name} getting URL: {url}")
        et = ET()
        requests.get(url)
        print(f"Task {name} total elapsed time: {et():.1f}")
        yield


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com"
    ]:
        work_queue.put(url)

    tasks = [
        task("One", work_queue),
        task("Two", work_queue)
    ]

    # run the tasks
    et = ET()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

    print(f"\nTotal elapsed time: {et():.1f}")


if __name__ == "__main__":
    main()
