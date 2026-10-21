from flask import Blueprint, render_template

from bloggy.db import get_db

bp = Blueprint("posts", __name__)


@bp.route("/")
def index():
    posts = get_db().execute("SELECT title, body FROM post ORDER BY id DESC")
    return render_template("posts/index.html", posts=posts.fetchall())
