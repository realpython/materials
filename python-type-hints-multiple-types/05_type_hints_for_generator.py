from collections.abc import Generator, Iterator


def parse_email() -> Generator[tuple[str, str], str, str]:
    sent = yield "", ""
    while sent != "":
        if "@" in sent:
            username, domain = sent.split("@")
            sent = yield username, domain
        else:
            sent = yield "ERROR", "invalid email"
    return "Done"


generator = parse_email()
next(generator)
generator.send("claudia@realpython.com")
generator.send("realpython")
try:
    generator.send("")
except StopIteration as ex:
    print(ex.value)


def parse_emails(emails: list[str]) -> Iterator[tuple[str, str]]:
    for email in emails:
        if "@" in email:
            username, domain = email.split("@")
            yield username, domain


# from collections.abc import Iterable
# def parse_emails(emails: Iterable[str]) -> Iterable[tuple[str, str]]:
#     for email in emails:
#         if "@" in email:
#             username, domain = email.split("@")
#             yield username, domain
