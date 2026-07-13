#!/usr/bin/env python3

from send_msg import send
from email.message import EmailMessage
from pathlib import Path

sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"

# Build Email Message
msg = EmailMessage()
msg["to"] = receiver_email
msg["from"] = sender_email
msg["subject"] = "Attachment Test Message"

text = "Please find a JPG attached."
msg.set_content(text)

attachment_file = Path("smiley-small.jpg")
with open(attachment_file, "rb") as attachment:
    # Add attachment to message
    msg.add_attachment(
        attachment.read(),
        maintype="image",
        subtype="jpeg",
        filename=attachment_file.name,
    )

# Send message
send(msg, sender_email)
