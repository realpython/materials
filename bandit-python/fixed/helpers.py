import ast
import hashlib
import json
import logging
import os
import secrets
import sqlite3
import subprocess
import tempfile

import requests
import yaml

logger = logging.getLogger(__name__)

API_KEY = os.environ["API_KEY"]
DB_PASSWORD = os.environ["DB_PASSWORD"]


def run_report(filename):
    subprocess.run(["sort", f"reports/{filename}"], check=True)  # nosec B603 B607 # noqa: S603, S607


def ping_host(host):
    return subprocess.check_output(["ping", "-c", "1", host])  # nosec B603 B607 # noqa: S603, S607


def make_token():
    return secrets.token_hex(16)


def hash_password(password, salt):
    return hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1
    ).hex()


def checksum(data):
    return hashlib.md5(data, usedforsecurity=False).hexdigest()


def load_config(text):
    return yaml.safe_load(text)


def parse_setting(text):
    return ast.literal_eval(text)


def load_session(blob):
    return json.loads(blob)


def fetch_status(url):
    return requests.get(url, timeout=10).status_code


def fetch_profile(url):
    return requests.get(url, timeout=10).json()


def write_cache(data):
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(data)
    return f.name


def find_user(conn: sqlite3.Connection, name):
    query = "SELECT * FROM users WHERE name = ?"
    return conn.execute(query, (name,)).fetchall()


def safe_int(value):
    try:
        return int(value)
    except ValueError:
        logger.warning("Not an integer: %r", value)
        return None


def parse_all(values):
    results = []
    for value in values:
        try:
            results.append(int(value))
        except ValueError:
            logger.warning("Skipping %r", value)
    return results


def check_admin(user):
    if not user.is_admin:
        raise PermissionError("Admin only")
    return True


def start_server(app):
    app.run(host="127.0.0.1", port=8000)
