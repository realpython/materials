import functools
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def timeit(function: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"{function.__name__}() finished in {end - start:.10f}s")
        return result

    return wrapper


@timeit
def parse_email(email_address: str) -> tuple[str, str]:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username, domain
    return "", ""


username, domain = parse_email("claudia@realpython.com")
print(username, domain)
