import time
from functools import wraps


def retry(delay=3, max_retries=3):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_retries + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Retrying in {delay}s... ({attempt}/{max_retries})")
                    time.sleep(delay)
            raise last_exc

        return wrapper

    return decorator
