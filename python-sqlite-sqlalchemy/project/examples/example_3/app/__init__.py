
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Define the application
app = Flask(__name__, instance_relative_config=False)

# Configure the application
app.config.from_object(Config)

# Define the database object
db = SQLAlchemy(app)

# Initialize Bootstrap connection
Bootstrap(app)

# Register Blueprings
from .artists import routes as artist_routes
from .albums import routes as album_routes
from .tracks import routes as track_routes
from .playlists import routes as playlist_routes
from .customers import routes as customer_routes
from .invoices import routes as invoice_routes
from .employees import routes as employee_routes
app.register_blueprint(artist_routes.artists_bp)
app.register_blueprint(album_routes.albums_bp)
app.register_blueprint(track_routes.tracks_bp)
app.register_blueprint(playlist_routes.playlists_bp)
app.register_blueprint(customer_routes.customers_bp)
app.register_blueprint(invoice_routes.invoices_bp)
app.register_blueprint(employee_routes.employees_bp)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app import models
