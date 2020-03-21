
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Define the application
app = Flask(__name__, instance_relative_config=False)

# Configure the application
app.config.from_object(Config)

# # Configurations
# app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Initialize Bootstrap connection
Bootstrap(app)

# Register Blueprings
from .artists import routes as artist_routes
from .albums import routes as album_routes
from .tracks import routes as track_routes
app.register_blueprint(artist_routes.artists_bp)
app.register_blueprint(album_routes.albums_bp)
app.register_blueprint(track_routes.tracks_bp)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
# app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..


#from app import routes
from app import models

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()

