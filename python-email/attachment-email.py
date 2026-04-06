#!/usr/bin/env python3

from send_msg import send
from email.message import EmailMessage
from os.path import basename

sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"

# Build Email Message
msg = EmailMessage()
msg["to"] = receiver_email
msg["from"] = sender_email
msg["subject"] = "Attachment Test Message"

text = "Please find a JPG attached."
msg.add_alternative(text, subtype="plain")

attachment_filename = "smiley-small.jpg"
with open("smiley-small.jpg", "rb") as attachment:
    attachment_data = attachment.read()
    attachment_file = basename(attachment_filename)
    msg.add_attachment(
        attachment_data, maintype="image", subtype="jpeg", filename=attachment_file
    )

# Send message
send(msg, sender_email)
