import time


def retry(delay=3, max_retries=3):
    def decorator(function):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return function(*args, **kwargs)
                except Exception:
                    attempts += 1
                    print(
                        f"Attempt {attempts} failed. Retrying in {delay}s..."
                    )
                    time.sleep(delay)

        return wrapper

    return decorator
