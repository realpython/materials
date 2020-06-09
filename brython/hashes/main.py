from browser import document, html, alert
import hashlib

hashes = {
    "sha-1": hashlib.sha1,
    "sha-256": hashlib.sha256,
    "sha-512": hashlib.sha512,
}


def compute_hash(evt):
    value = document["text-src"].value
    if not value:
        alert("You need to enter a value")
        return
    algo_dropdown = document["algo"]
    algo = algo_dropdown.options[algo_dropdown.selectedIndex].value
    hash_object = hashes[algo]()
    hash_object.update(value.encode())
    hex_value = hash_object.hexdigest()
    display_hash(hex_value)


def display_hash(hex_value):
    text = html.P(hex_value)
    hash_display = document["hash-display"]
    hash_display.clear()
    hash_display <= text


document["submit"].bind("click", compute_hash)
