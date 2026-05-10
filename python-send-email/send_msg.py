#!/usr/bin/env python3

import smtplib
import ssl
from getpass import getpass


def send(msg, sender_email, debug=True):
    if debug:
        port = 8025
        smtp_server = "localhost"
        with smtplib.SMTP(smtp_server, port) as server:
            server.send_message(msg)

    else:
        port = 465
        smtp_server = "smtp.gmail.com"
        password = getpass("Type your password and press enter: ")

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
