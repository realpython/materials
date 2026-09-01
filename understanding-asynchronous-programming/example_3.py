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
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

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
