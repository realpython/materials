import sqlite3
from dataclasses import astuple
from pathlib import Path

from bandcamp.storage.models import Track

DATABASE_PATH = Path.home() / "bandcamp.db"
SQL_CREATE = """\
    CREATE TABLE IF NOT EXISTS history (
        id TEXT PRIMARY KEY,
        title TEXT,
        artist TEXT,
        artist_url TEXT,
        album TEXT,
        album_url TEXT,
        genre TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
SQL_INSERT = """\
    INSERT INTO history (id, title, artist, artist_url, album, album_url, genre)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""
SQL_SELECT_ALL = "SELECT * FROM history"
SQL_SELECT_ONE = "SELECT id FROM history WHERE id=?"


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(SQL_CREATE)
        self.connection.commit()

    def persist(self, track: Track):
        self.cursor.execute(SQL_SELECT_ONE, (track.id,))
        if not self.cursor.fetchone():
            self.cursor.execute(SQL_INSERT, (track.id, *astuple(track)))
            self.connection.commit()

    def find_all(self):
        self.cursor.execute(SQL_SELECT_ALL)
        return [Track(*row[1:-1]) for row in self.cursor.fetchall()]

    def close(self):
        self.connection.close()
