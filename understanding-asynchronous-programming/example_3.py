import time
import queue
from lib.elapsed_time import ET


def task(name, queue):
    while not queue.empty():
        delay = queue.get()
        et = ET()
        print(f"Task {name} running")
        time.sleep(delay)
        print(f"Task {name} total elapsed time: {et():.1f}")
        yield


def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of 'work'
    work_queue = queue.Queue()

    # Put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
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
