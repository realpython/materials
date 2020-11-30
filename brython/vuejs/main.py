from browser import alert, window
from javascript import this
import hashlib

hashes = {
    "sha-1": hashlib.sha1,
    "sha-256": hashlib.sha256,
    "sha-512": hashlib.sha512,
}

Vue = window.Vue


def compute_hash(evt):
    value = this().input_text
    if not value:
        alert("You need to enter a value")
        return
    hash_object = hashes[this().algo]()
    hash_object.update(value.encode())
    hex_value = hash_object.hexdigest()
    this().hash_value = hex_value


def created():
    for name in hashes:
        this().algos.append(name)
    this().algo = next(iter(hashes))


app = Vue.createApp(
    {
        "el": "#app",
        "created": created,
        "data": lambda _: {
            "hash_value": "",
            "algos": [],
            "algo": "",
            "input_text": "",
        },
        "methods": {"compute_hash": compute_hash},
    }
)

app.mount("#app")
