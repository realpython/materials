emails = [
    " alice@example.org ",
    "BOB@example.com",
    "charlie@EXAMPLE.com",
    "David@example.net",
    " bob@example.com",
    "JohnDoe@example.com",
    "DAVID@Example.net",
]

# emails = [email.strip().lower() for email in emails]

emails = {email.strip().lower() for email in emails}
