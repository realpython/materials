from browser import document, html, alert
from browser.local_storage import storage
import base64


def load_data():
    b64_map = {}
    for key in storage.keys():
        b64_map[key] = storage.get(key)
    return b64_map


def save_data(key, value):
    storage[key] = value


def base64_compute(evt):
    key = document["text-src"].value
    if not key:
        alert("You need to enter a value")
        return
    if key in b64_map:
        alert(f"The base64 value of '{key}' already exists: '{b64_map[key]}'")
        return
    b64data = base64.b64encode(key.encode()).decode()
    b64_map[key] = b64data
    display_map()
    save_data(key, b64data)


def clear_map(evt):
    b64_map.clear()
    storage.clear()
    document["b64-display"].clear()


def display_map():
    if not b64_map:
        return
    table = html.TABLE(Class="pure-table")
    table <= html.THEAD(html.TR(html.TH("Text") + html.TH("Base64")))
    table <= (html.TR(html.TD(key) + html.TD(b64_map[key])) for key in b64_map)
    base64_display = document["b64-display"]
    base64_display.clear()
    base64_display <= table
    document["text-src"].value = ""


b64_map = load_data()
display_map()
document["submit"].bind("click", base64_compute)
document["clear-btn"].bind("click", clear_map)
