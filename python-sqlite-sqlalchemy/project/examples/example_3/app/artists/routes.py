from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError
from app import db
from app.models import Artist


# Setup the Blueprint
artists_bp = Blueprint(
    "artists_bp", __name__, template_folder="templates", static_folder="static"
)


def does_artist_exist(form, field):
    artist = (
        db.session.query(Artist)
        .filter(Artist.name == field.data)
        .one_or_none()
    )
    if artist is not None:
        raise ValidationError("Artist already exists", field.data)


class CreateArtistForm(FlaskForm):
    name = StringField(
        label="Artist's Name", validators=[InputRequired(), does_artist_exist]
    )


@artists_bp.route("/")
@artists_bp.route("/artists", methods=["GET", "POST"])
def artists():
    form = CreateArtistForm()

    # Is the form valid?
    if form.validate_on_submit():
        # Create new artist
        artist = Artist(name=form.name.data)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for("artists_bp.artists"))

    artists = db.session.query(Artist).order_by(Artist.name).all()
    return render_template("artists.html", artists=artists, form=form)
