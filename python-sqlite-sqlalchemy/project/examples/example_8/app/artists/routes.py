from flask import Blueprint
from flask import render_template
from app import db
from app.models import Artist


# Setup the Blueprint
artists_bp = Blueprint(
    "artists_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@artists_bp.route("/artists", methods=["GET"])
def artists():
    artists = db.session.query(Artist).all()
    return render_template("artists.html", artists=artists)
