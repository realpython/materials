import queue
import time

from codetiming import Timer


def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    while not work_queue.empty():
        delay = work_queue.get()
        print(f"Task {name} running")
        timer.start()
        time.sleep(delay)
        timer.stop()
        yield


def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

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
