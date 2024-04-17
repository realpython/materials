import sqlite3


def connect_to_db(db_path):
    return sqlite3.connect(db_path)


if __name__ == "__main__":
    connection = connect_to_db("birds.db")
    create_bird_table = """
    CREATE TABLE IF NOT EXISTS bird (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL
    );
    """
    connection.execute(create_bird_table)
    connection.close()
