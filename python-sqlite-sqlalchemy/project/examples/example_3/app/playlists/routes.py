from flask import Blueprint
from flask import render_template
from app import db
from app.models import Playlist


# Setup the Blueprint
playlists_bp = Blueprint(
    "playlists_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@playlists_bp.route("/playlists", methods=["GET"])
@playlists_bp.route("/playlists/<int:playlist_id>", methods=["GET"])
def playlists(playlist_id=None):

    # Start the query for playlists
    query = db.session.query(Playlist)

    # Display the tracks for the playlist passed?
    if playlist_id is not None:
        query = query.filter(Playlist.playlist_id == playlist_id)

    playlists = query.order_by(Playlist.name).all()

    return render_template("playlists.html", playlists=playlists)
