# stdlib imports
from os import environ as env

# 3rd party imports
from chalice import Chalice, Response
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Twilio Config
ACCOUNT_SID = env.get('ACCOUNT_SID')
AUTH_TOKEN = env.get('AUTH_TOKEN')
FROM_NUMBER = env.get('FROM_NUMBER')
TO_NUMBER = env.get('TO_NUMBER')

app = Chalice(app_name='serverless-sms-service')

# create a twilio client using account_sid and auth token
tw_client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/service/sms/send', methods=['POST'])
def send_sms():
    request_body = app.current_request.json_body
    if request_body:
        try:
            msg = tw_client.messages.create(
                from_=FROM_NUMBER,
                body=request_body['msg'],
                to=TO_NUMBER)
            if msg.sid:
                return Response(status_code=201,
                                headers={'Content-Type': 'application/json'},
                                body={'status': 'success',
                                      'data': msg.sid,
                                      'message': 'SMS successfully sent'})
            else:
                return Response(status_code=200,
                                headers={'Content-Type': 'application/json'},
                                body={'status': 'failure',
                                      'message': 'Please try again!!!'})
        except TwilioRestException as exc:
            return Response(status_code=400,
                            headers={'Content-Type': 'application/json'},
                            body={'status': 'failure',
                                  'message': exc.msg})
