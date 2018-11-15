from os import environ as env
from twilio.rest import Client

# Twilio Config
ACCOUNT_SID = env.get("ACCOUNT_SID")
AUTH_TOKEN = env.get("AUTH_TOKEN")
FROM_NUMBER = env.get("FROM_NUMBER")
TO_NUMBER = env.get("TO_NUMBER")

# create a twilio client using account_sid and auth token
tw_client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send(payload_params=None):
    """ send sms to the specified number """
    msg = tw_client.messages.create(
        from_=FROM_NUMBER, body=payload_params["msg"], to=TO_NUMBER
    )

    if msg.sid:
        return msg
