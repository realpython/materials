#!/usr/bin/env python3

from send_msg import send
from email.message import EmailMessage

sender_email = "my@gmail.com"
receiver_email_1 = "your@gmail.com"
receiver_email_2 = "your_other@gmail.com"
cc_receiver_email = "cc-you@gmail.com"
bcc_receiver_email = "bcc-you@gmail.com"

# Build Email Message
msg = EmailMessage()
msg["to"] = [receiver_email_1, receiver_email_2]
msg["cc"] = cc_receiver_email
msg["bcc"] = bcc_receiver_email
msg["from"] = sender_email
msg["subject"] = "Test Message"
msg.set_content("This is a test message")

# Send message
send(msg, sender_email)
