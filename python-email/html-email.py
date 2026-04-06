#!/usr/bin/env python3

from send_msg import send
from email.message import EmailMessage

sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"

# Build Email Message
msg = EmailMessage()
msg["to"] = receiver_email
msg["from"] = sender_email
msg["subject"] = "HTML Test Message"

text = """\
Hi,
How are you?
Real Python has many great tutorials:
realpython.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://realpython.com">Real Python</a>
       has many great tutorials.
    </p>
  </body>
</html>
"""

msg.set_content(text)
msg.add_alternative(html, subtype="html")

# Send message
send(msg, sender_email)
