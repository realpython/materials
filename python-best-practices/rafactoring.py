# Avoid this:
# def find_duplicate_emails(users):
#     duplicates = []
#     seen = []
#     for user in users:
#         email = user.get("email")

#         if email is None:
#             print("Missing email for", user.get("id"))
#             continue

#         # Check if we've seen this email before
#         already_seen = False
#         for index in range(len(seen)):
#             if seen[index] == email:
#                 already_seen = True
#                 break

#         if already_seen:
#             duplicates.append(email)
#         else:
#             seen.append(email)

#     print("Found", len(duplicates), "duplicate emails")
#     return duplicates


# Favor this:
from collections import Counter


def _extract_emails(users):
    return [user["email"] for user in users if "email" in user]


def find_duplicate_emails(users):
    emails = _extract_emails(users)
    counts = Counter(emails)
    return [email for email, count in counts.items() if count > 1]
