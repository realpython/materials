import json
from base64 import b64decode
from pathlib import Path

JSON_FILE = Path("An ec-1668602437.json")
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem
DATA_DIR = Path.cwd() / "responses"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(DATA_DIR / JSON_FILE, "r") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    with open(IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png", "wb") as png_file:
        png_file.write(image_data)
