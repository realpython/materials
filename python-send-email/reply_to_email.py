#!/usr/bin/env python3

from send_msg import send
from email.message import EmailMessage

sender_email = "my@gmail.com"
reply_email = "my.different@gmail.com"
receiver_email = "your@gmail.com"

# Build Email Message
msg = EmailMessage()
msg["to"] = receiver_email
msg["from"] = sender_email
msg["reply-to"] = reply_email
msg["subject"] = "Reply Please"
msg.set_content("Replies go to a different mailbox.")

# Send message
send(msg, sender_email)
