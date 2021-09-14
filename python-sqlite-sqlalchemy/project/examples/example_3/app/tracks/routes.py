from flask import Blueprint
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms import FloatField
from wtforms import SelectField
from wtforms import HiddenField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError
from app import db
from app.models import Artist
from app.models import Album
from app.models import Track
from app.models import MediaType
from app.models import Genre


# Setup the Blueprint
tracks_bp = Blueprint(
    "tracks_bp", __name__, template_folder="templates", static_folder="static"
)


def does_artist_exist(form, field):
    artist = (
        db.session.query(Artist)
        .filter(Artist.name == field.data)
        .one_or_none()
    )

    if artist is not None:
        raise ValidationError("Artist already exists", field.data)


def does_album_exist(form, field):
    album = (
        db.session.query(Album).filter(Album.title == field.data).one_or_none()
    )

    if album is not None:
        raise ValidationError("Album already exists", field.data)


def does_track_exist(form, field):
    track = (
        db.session.query(Track)
        .join(Album)
        .join(Artist)
        .filter(Artist.name == form.artist.data)
        .filter(Album.title == form.album.data)
        .filter(Track.name == field.data)
        .one_or_none()
    )

    if track is not None:
        raise ValidationError("Track already exists", field.data)


class CreateTrackForm(FlaskForm):
    artist = HiddenField("artist")
    album = HiddenField("album")
    name = StringField(
        label="Track's Name", validators=[InputRequired(), does_track_exist]
    )
    media_type = SelectField(label="Media Type", validators=[InputRequired()])
    genre = SelectField(label="Genre", validators=[InputRequired()])
    composer = StringField(label="Composer")
    milliseconds = IntegerField(
        label="Time in Milliseconds", validators=[InputRequired()]
    )
    bytes = IntegerField(label="Size in Bytes", validators=[InputRequired()])
    unit_price = FloatField(label="Unit Price", validators=[InputRequired()])


@tracks_bp.route("/tracks/<int:album_id>", methods=["GET", "POST"])
def tracks(album_id=None):
    form = CreateTrackForm()

    # Get MediaType information and populate the form
    form.media_type.choices = [
        (str(media_type.media_type_id), media_type.name)
        for media_type in MediaType.query.order_by(MediaType.media_type_id)
    ]

    # Get Genre information and populate the form
    form.genre.choices = [
        (str(genre.genre_id), genre.name)
        for genre in Genre.query.order_by(Genre.genre_id)
    ]

    # Get the album
    album = (
        db.session.query(Album)
        .filter(Album.album_id == album_id)
        .one_or_none()
    )
    form.album.data = album.title

    artist = album.artist
    form.artist.data = artist.name

    # Is the form valid?
    if form.validate_on_submit():
        # Create new Track
        track = Track(
            name=form.name.data,
            media_type_id=form.media_type.data,
            genre_id=form.genre.data,
            composer=form.composer.data,
            milliseconds=form.milliseconds.data,
            bytes=form.bytes.data,
            unit_price=form.unit_price.data,
        )
        album.tracks.append(track)
        db.session.add(album)
        db.session.commit()

    # Get the tracks
    tracks = db.session.query(Track).filter(Track.album_id == album_id).all()

    return render_template(
        "tracks.html", artist=artist, album=album, tracks=tracks, form=form
    )
