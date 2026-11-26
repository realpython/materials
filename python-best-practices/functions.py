# Avoid this:
# import csv

# def process_users(users, min_age, filename, send_email):
#     adults = []
#     for user in users:
#         if user["age"] >= min_age:
#             adults.append(user)

#     with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(["name", "age"])
#         for user in adults:
#             writer.writerow([user["name"], user["age"]])

#     if send_email:
#         # Emailing logic here...

#     return adults, filename

# Favor this:
import csv


def filter_adult_users(users, *, min_age=18):
    """Return users whose age is at least min_age."""
    return [user for user in users if user["age"] >= min_age]


def save_users_csv(users, filename):
    """Save users to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["name", "age"])
        for user in users:
            writer.writerow([user["name"], user["age"]])


def send_users_report(filename):
    """Send the report."""
    # Emailing logic here...
