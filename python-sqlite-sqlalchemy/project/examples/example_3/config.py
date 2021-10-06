import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load the environment variables from .env file
path = Path(__file__).parent / ".env"
if path.exists():
    load_dotenv()
else:
    raise IOError(".env file not found")


class Config:
    base_path = Path(__file__).resolve().parent.parent.parent
    db_path = base_path / "data" / "chinook.db"

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{str(db_path)}"
    SQLALCHEMY_TRACK_MODIFICATIONS = json.loads(
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS").lower()
    )
    SQLALCHEMY_ECHO = json.loads(os.getenv("SQLALCHEMY_ECHO").lower())
    DEBUG = json.loads(os.getenv("DEBUG").lower())
