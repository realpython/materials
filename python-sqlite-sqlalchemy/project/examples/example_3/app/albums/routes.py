from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, ValidationError
from app import db
from app.models import Artist, Album


# Setup the Blueprint
albums_bp = Blueprint(
    "albums_bp", __name__, template_folder="templates", static_folder="static"
)


def does_album_exist(form, field):
    album = (
        db.session.query(Album).filter(Album.title == field.data).one_or_none()
    )

    if album is not None:
        raise ValidationError("Album already exists", field.data)


class CreateAlbumForm(FlaskForm):
    title = StringField(
        label="Albums's Name", validators=[InputRequired(), does_album_exist]
    )


@albums_bp.route("/albums", methods=["GET", "POST"])
@albums_bp.route("/albums/<int:artist_id>", methods=["GET", "POST"])
def albums(artist_id=None):
    form = CreateAlbumForm()

    # Get the artist
    artist = (
        db.session.query(Artist)
        .filter(Artist.artist_id == artist_id)
        .one_or_none()
    )

    # Is the form valid?
    if form.validate_on_submit():
        # Create new Album
        album = Album(title=form.title.data)
        artist.albums.append(album)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for("albums_bp.albums", artist_id=artist_id))

    # Start the query for albums
    query = db.session.query(Album)

    # Display the albums for the artist passed?
    if artist_id is not None:
        query = query.filter(Album.artist_id == artist_id)

    albums = query.order_by(Album.title).all()

    return render_template(
        "albums.html", artist=artist, albums=albums, form=form
    )
