import collections
import logging
import random
import threading
import time

logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")


class SynchronizedBuffer:
    def __init__(self, capacity):
        self.values = collections.deque(maxlen=capacity)
        self.lock = threading.RLock()
        self.consumed = threading.Condition(self.lock)
        self.produced = threading.Condition(self.lock)

    def __repr__(self):
        return repr(list(self.values))

    @property
    def empty(self):
        return len(self.values) == 0

    @property
    def full(self):
        return len(self.values) == self.values.maxlen

    def put(self, value):
        with self.lock:
            self.consumed.wait_for(lambda: not self.full)
            self.values.append(value)
            self.produced.notify()

    def get(self):
        with self.lock:
            self.produced.wait_for(lambda: not self.empty)
            try:
                return self.values.popleft()
            finally:
                self.consumed.notify()


def producer(buffer):
    while True:
        value = random.randint(1, 10)
        buffer.put(value)
        logging.info("produced %d: %s", value, buffer)
        time.sleep(random.random())


def consumer(buffer):
    while True:
        value = buffer.get()
        logging.info("consumed %d: %s", value, buffer)
        time.sleep(random.random())


if __name__ == "__main__":

    buffer = SynchronizedBuffer(5)

    for _ in range(3):
        threading.Thread(target=producer, args=(buffer,)).start()

    for _ in range(2):
        threading.Thread(target=consumer, args=(buffer,)).start()
