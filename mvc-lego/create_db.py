"""Creates and seeds a SQLite example database."""

import sqlite3

DATABASE = "./database.db"

with sqlite3.connect(DATABASE) as db:
    try:
        # Create a table in the database
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                text TEXT
            );
        """
        )

        # Insert a new entry to the database
        cursor.execute(
            """
            INSERT INTO entries (title, text) VALUES (?, ?)
        """,
            ("spaceship", "My MVP MVC Lego spaceship 🚀"),
        )

        db.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
