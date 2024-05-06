import os

from dotenv import load_dotenv
from flask import Flask

from board import (
    database,
    errors,
    pages,
    posts,
)

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    # app.logger.setLevel("INFO")

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)
    app.logger.debug(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    app.logger.debug(f"Using Database: {app.config.get('DATABASE')}")
    return app
