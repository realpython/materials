import os
from pathlib import Path

base_path = Path(__file__).resolve().parent
db_path = base_path / "app" / "data" / "chinook.db"


class Config:
    SECRET_KEY = "you-will-never-guess"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
