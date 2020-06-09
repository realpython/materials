from browser import document, html, alert
from browser.local_storage import storage
import json
import hashlib

LOCAL_STORAGE = "hashdata"


def load_data():
    data = storage.get(LOCAL_STORAGE)
    if data:
        hash_map = json.loads(data)
    else:
        storage[LOCAL_STORAGE] = json.dumps({})
        hash_map = {}
    return hash_map


def compute(evt):
    value = document["text-src"].value
    if not value:
        alert("You need to enter a value")
        return
    if value in hash_map:
        alert(
            f"The SHA-256 value of '{value}' "
            f"already exists: '{hash_map[value]}'"
        )
        return
    hash = hashlib.sha256()
    hash.update(value.encode())
    hash_hex = hash.hexdigest()
    hash_map[value] = hash_hex
    storage[LOCAL_STORAGE] = json.dumps(hash_map)
    display_map()


def clear_map(evt):
    hash_map.clear()
    storage[LOCAL_STORAGE] = json.dumps({})
    document["hash-display"].clear()


def display_map():
    if not hash_map:
        return
    table = html.TABLE(Class="pure-table")
    table <= html.THEAD(html.TR(html.TH("Text") + html.TH("SHA-256")))
    table <= (
        html.TR(html.TD(key) + html.TD(hash_map[key])) for key in hash_map
    )
    hash_display = document["hash-display"]
    hash_display.clear()
    hash_display <= table
    document["text-src"].value = ""


hash_map = load_data()
display_map()
document["submit"].bind("click", compute)
document["clear-btn"].bind("click", clear_map)
