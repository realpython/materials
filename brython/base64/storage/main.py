from browser import document, html, alert
from browser.local_storage import storage
import json
import base64


def load_data():
    data = storage.get("b64data")
    if data:
        b64_map = json.loads(data)
    else:
        storage["b64data"] = json.dumps({})
        b64_map = {}
    return b64_map


def base64_compute(evt):
    value = document["text-src"].value
    if not value:
        alert("You need to enter a value")
        return
    if value in b64_map:
        alert(
            f"The base64 value of '{value}' already exists: '{b64_map[value]}'"
        )
        return
    b64data = base64.b64encode(value.encode()).decode()
    b64_map[value] = b64data
    storage["b64data"] = json.dumps(b64_map)
    display_map()


def clear_map(evt):
    b64_map.clear()
    storage["b64data"] = json.dumps({})
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
