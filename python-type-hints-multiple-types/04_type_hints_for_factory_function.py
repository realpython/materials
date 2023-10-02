import functools
import time
from collections.abc import Callable
from typing import Any


def timeit(function: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"{function.__name__}() finished in {end - start:.10f}s")
        return result

    return wrapper


@timeit
def parse_email(email_address: str) -> tuple[str, str] | None:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username, domain
    return None


username, domain = parse_email("claudia@realpython.com")
print(username, domain)
