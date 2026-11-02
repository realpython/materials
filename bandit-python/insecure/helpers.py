import hashlib
import pickle
import random
import subprocess
import tempfile
import yaml
import requests

API_KEY = "sk-live-4f9a8b7c6d5e4f3a2b1c"
DB_PASSWORD = "admin123"


def run_report(filename):
    subprocess.run(f"cat reports/{filename} | sort", shell=True)


def ping_host(host):
    return subprocess.check_output("ping -c 1 " + host, shell=True)


def make_token():
    return "".join(random.choice("abcdef0123456789") for _ in range(32))


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def load_config(text):
    return yaml.load(text, Loader=yaml.Loader)


def parse_setting(text):
    return eval(text)


def load_session(blob):
    return pickle.loads(blob)


def fetch_status(url):
    response = requests.get(url, verify=False)
    return response.status_code


def fetch_profile(url):
    return requests.get(url).json()


def write_cache(data):
    path = tempfile.mktemp()
    with open(path, "w") as f:
        f.write(data)
    return path


def find_user(conn, name):
    query = "SELECT * FROM users WHERE name = '%s'" % name
    return conn.execute(query).fetchall()


def safe_int(value):
    try:
        return int(value)
    except Exception:
        pass


def parse_all(values):
    results = []
    for value in values:
        try:
            results.append(int(value))
        except:
            continue
    return results


def check_admin(user):
    assert user.is_admin, "Admin only"
    return True


def start_server(app):
    app.run(host="0.0.0.0", port=8000)
