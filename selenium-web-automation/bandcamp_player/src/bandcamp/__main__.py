from bandcamp.tui.app import BandcampApp
from bandcamp.workers.messages import Message
from bandcamp.workers.storage import StorageWorker
from bandcamp.workers.web import WebWorker


def main() -> None:
    storage_worker = StorageWorker()
    storage_worker.start()
    web_worker = WebWorker()
    web_worker.start()
    try:
        BandcampApp(storage_worker, web_worker).run()
    finally:
        storage_worker.inbox.put(Message.GRACEFUL_STOP)
        web_worker.inbox.put(Message.GRACEFUL_STOP)


if __name__ == "__main__":
    main()
