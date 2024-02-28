import sqlite3

from flask import Flask, g, render_template

DATABASE = "./database.db"

app = Flask(__name__)


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route("/")
def home():
    """Searches the database for entries, then displays them."""
    db = get_db()
    cur = db.execute("SELECT * FROM entries ORDER BY id DESC;")
    entries = cur.fetchall()
    print(entries)
    return render_template("index.html", entries=entries)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
