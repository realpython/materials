from typing import Union


def parse_email(email_address: str) -> str | None:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username
    return None


def parse_email(email_address: str) -> Union[str, None]:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username
    return None