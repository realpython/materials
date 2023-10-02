from collections.abc import Callable
from typing import Any

def apply_func(
	func: Callable[..., Any], *args: Any
) -> Any:
	return func(*args)

def parse_email(email_address: str) -> tuple[str, str] | None:
	if "@" in email_address:
		username, domain = email_address.split("@")
		return username, domain
	return None

apply_funct(parse_email, "claudia@realpython.com")