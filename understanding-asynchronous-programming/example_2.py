import queue


def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        print(f"Task {name} running")
        for _ in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")


def main():
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    while tasks:
        for current_task in tasks.copy():
            try:
                next(current_task)
            except StopIteration:
                tasks.remove(current_task)


if __name__ == "__main__":
    main()
