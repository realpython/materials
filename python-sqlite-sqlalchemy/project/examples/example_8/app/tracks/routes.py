from flask import Blueprint
from flask import render_template
from app import db
from app.models import Track


# Setup the Blueprint
tracks_bp = Blueprint(
    "tracks_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@tracks_bp.route("/tracks/<int:album_id>", methods=["GET"])
def tracks(album_id=None):
    # get the tracks
    tracks = db.session.query(Track) \
        .filter(Track.album_id == album_id) \
        .all()

    return render_template(
        "tracks.html", 
        tracks=tracks
    )
