from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def apply_func(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    return func(*args, **kwargs)


def parse_email(email_address: str) -> tuple[str, str]:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username, domain
    return "", ""


apply_func(parse_email, "claudia@realpython.com")
