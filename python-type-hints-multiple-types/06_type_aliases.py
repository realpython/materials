from typing import TypeAlias


EmailComponents = tuple[str, str] | None


def parse_email(email_address: str) -> EmailComponents:
	if "@" in email_address:
		username, domain = email_address.split("@")
		return username, domain
	return None


EmailComponents: TypeAlias = tuple[str, str] | None
type EmailComponents = tuple[str, str] | None