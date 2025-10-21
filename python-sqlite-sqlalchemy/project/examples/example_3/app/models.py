# coding: utf-8

from app import db
from sqlalchemy.ext.hybrid import hybrid_property


class Artist(db.Model):
    __tablename__ = "artists"
    artist_id = db.Column("ArtistId", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(120))
    albums = db.relationship("Album", backref="artist")


class Employee(db.Model):
    __tablename__ = "employees"
    employee_id = db.Column("EmployeeId", db.Integer, primary_key=True)
    last_name = db.Column("LastName", db.String(20), nullable=False)
    first_name = db.Column("FirstName", db.String(20), nullable=False)
    title = db.Column("Title", db.String(30))
    reports_to_id = db.Column(
        "ReportsTo", db.ForeignKey("employees.EmployeeId"), index=True
    )
    reports_to = db.relationship(
        "Employee", uselist=False, remote_side=[employee_id]
    )
    birth_date = db.Column("BirthDate", db.DateTime)
    hire_date = db.Column("HireDate", db.DateTime)
    address = db.Column("Address", db.String(70))
    city = db.Column("City", db.String(40))
    state = db.Column("State", db.String(40))
    country = db.Column("Country", db.String(40))
    postal_code = db.Column("PostalCode", db.String(10))
    phone = db.Column("Phone", db.String(24))
    fax = db.Column("Fax", db.String(24))
    email = db.Column("Email", db.String(60))
    parent = db.relationship(
        "Employee", remote_side=[employee_id], backref="reporting"
    )

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(db.Model):
    __tablename__ = "genres"
    genre_id = db.Column("GenreId", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(120))
    tracks = db.relationship("Track", backref="genre")


class MediaType(db.Model):
    __tablename__ = "media_types"
    media_type_id = db.Column("MediaTypeId", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(120))
    tracks = db.relationship("Track", backref="media_type")


class Playlist(db.Model):
    __tablename__ = "playlists"
    playlist_id = db.Column("PlaylistId", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(120))
    tracks = db.relationship(
        "Track", secondary="playlist_track", back_populates="playlists"
    )


class Album(db.Model):
    __tablename__ = "albums"
    album_id = db.Column("AlbumId", db.Integer, primary_key=True)
    title = db.Column("Title", db.String(160), nullable=False)
    artist_id = db.Column(
        "ArtistId",
        db.ForeignKey("artists.ArtistId"),
        nullable=False,
        index=True,
    )
    tracks = db.relationship("Track", backref="album")


class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column("CustomerId", db.Integer, primary_key=True)
    first_name = db.Column("FirstName", db.String(40), nullable=False)
    last_name = db.Column("LastName", db.String(20), nullable=False)
    company = db.Column("Company", db.String(80))
    address = db.Column("Address", db.String(70))
    city = db.Column("City", db.String(40))
    state = db.Column("State", db.String(40))
    country = db.Column("Country", db.String(40))
    postal_code = db.Column("PostalCode", db.String(10))
    phone = db.Column("Phone", db.String(24))
    fax = db.Column("Fax", db.String(24))
    email = db.Column("Email", db.String(60), nullable=False)
    support_rep_id = db.Column(
        "SupportRepId", db.ForeignKey("employees.EmployeeId"), index=True
    )
    support_rep = db.relationship(
        "Employee", backref=db.backref("customers", uselist=False)
    )
    invoices = db.relationship("Invoice", backref="customer")

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Invoice(db.Model):
    __tablename__ = "invoices"
    invoice_id = db.Column("InvoiceId", db.Integer, primary_key=True)
    customer_id = db.Column(
        "CustomerId",
        db.ForeignKey("customers.CustomerId"),
        nullable=False,
        index=True,
    )
    invoice_date = db.Column("InvoiceDate", db.DateTime, nullable=False)
    billing_address = db.Column("BillingAddress", db.String(70))
    billing_city = db.Column("BillingCity", db.String(40))
    billing_state = db.Column("BillingState", db.String(40))
    billing_country = db.Column("BillingCountry", db.String(40))
    billing_postal_code = db.Column("BillingPostalCode", db.String(10))
    total = db.Column("Total", db.Float, nullable=False)
    invoice_items = db.relationship("InvoiceItem", backref="invoice")


class Track(db.Model):
    __tablename__ = "tracks"

    track_id = db.Column("TrackId", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(200), nullable=False)
    album_id = db.Column(
        "AlbumId", db.ForeignKey("albums.AlbumId"), index=True
    )
    media_type_id = db.Column(
        "MediaTypeId",
        db.ForeignKey("media_types.MediaTypeId"),
        nullable=False,
        index=True,
    )
    genre_id = db.Column(
        "GenreId", db.ForeignKey("genres.GenreId"), index=True
    )
    composer = db.Column("Composer", db.String(220))
    milliseconds = db.Column("Milliseconds", db.Integer, nullable=False)
    bytes = db.Column("Bytes", db.Integer)
    unit_price = db.Column("UnitPrice", db.Float, nullable=False)
    invoice_items = db.relationship("InvoiceItem", backref="track")
    playlists = db.relationship(
        "Playlist", secondary="playlist_track", back_populates="tracks"
    )


class InvoiceItem(db.Model):
    __tablename__ = "invoice_items"
    invoice_line_id = db.Column("InvoiceLineId", db.Integer, primary_key=True)
    invoice_id = db.Column(
        "InvoiceId",
        db.ForeignKey("invoices.InvoiceId"),
        nullable=False,
        index=True,
    )
    track_id = db.Column(
        "TrackId", db.ForeignKey("tracks.TrackId"), nullable=False, index=True
    )
    unit_price = db.Column("UnitPrice", db.Float, nullable=False)
    quantity = db.Column("Quantity", db.Integer, nullable=False)


playlist_track = db.Table(
    "playlist_track",
    db.Column(
        "PlaylistId",
        db.Integer,
        db.ForeignKey("playlists.PlaylistId"),
        primary_key=True,
        nullable=False,
    ),
    db.Column(
        "TrackId",
        db.Integer,
        db.ForeignKey("tracks.TrackId"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)
