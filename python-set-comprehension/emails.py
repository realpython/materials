emails = {
    " alice@example.org ",
    "BOB@example.com",
    "charlie@EXAMPLE.com",
    "David@example.net",
    " bob@example.com",
    "JohnDoe@example.com",
}

print({email.strip().lower() for email in emails})
