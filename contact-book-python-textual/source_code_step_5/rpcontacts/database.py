import pathlib
import sqlite3

DATABASE_PATH = pathlib.Path().home() / "contacts.db"


class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                email TEXT
            );
        """
        self._run_query(query)

    def _run_query(self, query, *query_args):
        result = self.cursor.execute(query, [*query_args])
        self.db.commit()
        return result

    def get_all_contacts(self):
        result = self._run_query("SELECT * FROM contacts;")
        return result.fetchall()

    def get_last_contact(self):
        result = self._run_query(
            "SELECT * FROM contacts ORDER BY id DESC LIMIT 1;"
        )
        return result.fetchone()

    def add_contact(self, contact):
        self._run_query(
            "INSERT INTO contacts VALUES (NULL, ?, ?, ?);",
            *contact,
        )

    def delete_contact(self, id):
        self._run_query(
            "DELETE FROM contacts WHERE id=(?);",
            id,
        )

    def clear_all_contacts(self):
        self._run_query("DELETE FROM contacts;")


data = [
    ("Linda", "111-2222-3333", "linda@example.com"),
    ("Joe", "111-2222-3333", "joe@example.com"),
    ("Lara", "111-2222-3333", "lara@example.com"),
    ("David", "111-2222-3333", "david@example.com"),
    ("Jane", "111-2222-3333", "jane@example.com"),
]
