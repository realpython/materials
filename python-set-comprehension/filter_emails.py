emails_set = {
    "alice@example.org",
    "bob@example.com",
    "johndoe@example.com",
    "charlie@example.com",
    "david@example.net",
}

print({email for email in emails_set if email.endswith(".com")})
