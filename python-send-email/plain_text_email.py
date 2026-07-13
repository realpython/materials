#!/usr/bin/env python3

from send_msg import send
from email.message import EmailMessage

sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"

# Build Email Message
msg = EmailMessage()
msg["to"] = receiver_email
msg["from"] = sender_email
msg["subject"] = "Test Message"
msg.set_content("This is a test message")

# Send message
send(msg, sender_email)
