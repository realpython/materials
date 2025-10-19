from board import pages
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    return app
