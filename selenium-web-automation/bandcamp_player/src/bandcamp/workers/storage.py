import queue
import threading

from bandcamp.storage.database import Database
from bandcamp.workers.messages import Message


class StorageWorker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.inbox = queue.Queue()

    def run(self):
        database = Database()
        try:
            while True:
                match self.inbox.get():
                    case Message.GRACEFUL_STOP:
                        break
                    case track:
                        database.persist(track)
                        self.inbox.task_done()
        finally:
            if database:
                database.close()
