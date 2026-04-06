#!/usr/bin/env python3

import csv

from send_msg import send
from email.message import EmailMessage
from email.headerregistry import Address

sender_email = "my@gmail.com"
sender = Address(display_name="Me", addr_spec=sender_email)

with open("contacts.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email, grade in reader:
        recipient = Address(display_name=name, addr_spec=email)
        msg = EmailMessage()
        msg["to"] = recipient
        msg["from"] = sender
        msg["Subject"] = "Your grade"
        msg.set_content(f"Congratulations, {name}, you got a {grade}.")

        send(msg, sender_email)
