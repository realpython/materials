from flask import Blueprint
from flask import render_template
from app import db
from app.models import Album


# Setup the Blueprint
albums_bp = Blueprint(
    "albums_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@albums_bp.route("/albums", methods=["GET"])
@albums_bp.route("/albums/<int:artist_id>", methods=["GET"])
def albums(artist_id=None):
    # Start the query for albums
    query = db.session.query(Album)

    # Display the albums for the artist passed?
    if artist_id is not None:
        query = query.filter(Album.artist_id == artist_id)

    albums = query.all()

    return render_template(
        "albums.html", 
        artist_id=artist_id,
        albums=albums
    )
