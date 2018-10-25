from chalice import Chalice

app = Chalice(app_name='serverless-sms-service')


@app.route('/')
def index():
    return {'hello': 'world'}
