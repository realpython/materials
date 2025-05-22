emails = [
    " alice@example.org ",
    "BOB@example.com",
    "charlie@EXAMPLE.com",
    "David@example.net",
    " bob@example.com",
    "JohnDoe@example.com",
    "DAVID@Example.net",
]

clean_emails = [email.strip().lower() for email in emails]
print(clean_emails)

unique_emails = {email.strip().lower() for email in emails}
print(unique_emails)
