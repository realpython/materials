import queue


def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")


def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # Create some tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    while tasks:
        for t in tasks.copy():
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)


if __name__ == "__main__":
    main()
