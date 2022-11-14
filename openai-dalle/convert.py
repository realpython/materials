import json
from base64 import b64decode
from pathlib import Path

JSON_FILE_NAME = "An ec-1667994848"
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE_NAME
DATA_DIR = Path.cwd() / "responses"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(DATA_DIR / f"{JSON_FILE_NAME}.json", "r") as f:
    response = json.load(f)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    with open(IMAGE_DIR / f"{JSON_FILE_NAME}-{index}.png", "wb") as f:
        f.write(image_data)
