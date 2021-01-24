import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))


@app.route("/")
def index():
    return f"The configured secret key is {app.config.get('SECRET_KEY')}"
