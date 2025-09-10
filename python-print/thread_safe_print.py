import threading

lock = threading.Lock()


def thread_safe_print(*args, **kwargs):
    with lock:
        print(*args, **kwargs)
