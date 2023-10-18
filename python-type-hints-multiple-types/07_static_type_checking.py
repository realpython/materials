def parse_email(email_address: str) -> tuple[str, str] | None:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username, domain
    return None
