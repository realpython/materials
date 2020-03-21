import os
from pathlib import Path
from dotenv import load_dotenv

base_path = Path(__file__).resolve().parent
db_path = base_path / "app" / "data" / "chinook.db"

load_dotenv()

class Config:
    SECRET_KEY = "you-will-never-guess"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False



    # SECRET_KEY = os.getenv("SECRET_KEY")

    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(db_path)
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    # SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO")

    DEBUG = True
