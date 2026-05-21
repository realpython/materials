import logging
import threading

WORKER_INTERVAL = 1  # Seconds between worker check-ins
MAIN_INTERVAL = 0.75  # Seconds between main thread check-ins


def worker(event):
    while not event.is_set():
        logging.debug("Worker thread checking in")
        event.wait(WORKER_INTERVAL)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="{relativeCreated:>6,.0f} ms | {threadName:<18} | {message}",
        style="{",
    )
    event = threading.Event()

    thread_one = threading.Thread(target=worker, args=(event,))
    thread_two = threading.Thread(target=worker, args=(event,))
    thread_one.start()
    thread_two.start()

    while not event.is_set():
        try:
            logging.debug("Main thread checking in")
            event.wait(MAIN_INTERVAL)
        except KeyboardInterrupt:
            event.set()
            break


if __name__ == "__main__":
    main()
