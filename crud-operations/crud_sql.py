import sqlite3


def connect_to_db(db_path):
    return sqlite3.connect(db_path)


if __name__ == "__main__":
    with connect_to_db("birds.db") as connection:
        connection.execute(
            """
          CREATE TABLE IF NOT EXISTS bird (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
          );
        """
        )
