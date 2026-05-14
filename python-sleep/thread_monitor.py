import logging
import threading

WORKER_INTERVAL = 1  # Seconds between worker check-ins
MAIN_INTERVAL = 0.75  # Seconds between main thread check-ins


def worker(event):
    while not event.is_set():
        logging.debug("worker thread checking in")
        event.wait(WORKER_INTERVAL)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(relativeCreated)6d %(threadName)s %(message)s",
    )
    event = threading.Event()

    thread = threading.Thread(target=worker, args=(event,))
    thread_two = threading.Thread(target=worker, args=(event,))
    thread.start()
    thread_two.start()

    while not event.is_set():
        try:
            logging.debug("Checking in from main thread")
            event.wait(MAIN_INTERVAL)
        except KeyboardInterrupt:
            event.set()
            break


if __name__ == "__main__":
    main()
