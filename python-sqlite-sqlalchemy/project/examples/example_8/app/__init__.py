
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

# define the application
app = Flask(__name__)

# configure the application
app.config.from_object(Config)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

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


from app import routes
from app import models

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

