from pathlib import Path

from flask import Flask


def create_app(test_config=None):
    """Create and configure the Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=str(Path(app.instance_path) / "bloggy.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    from bloggy import auth, db, posts

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(posts.bp)

    return app
