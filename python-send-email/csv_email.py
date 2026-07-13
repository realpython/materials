#!/usr/bin/env python3

import csv
from email.message import EmailMessage

from send_msg import send

sender_email = "my@gmail.com"

with open("contacts.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email, grade in reader:
        msg = EmailMessage()
        msg["to"] = f"{name} <{email}>"
        msg["from"] = f"Me <{sender_email}>"
        msg["Subject"] = "Your grade"
        msg.set_content(f"Congratulations, {name}, you got a {grade}.")

        send(msg, sender_email)
