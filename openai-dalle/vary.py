import json
import os
from base64 import b64decode
from pathlib import Path

import openai

SOURCE_FILE = "A com-1667994848.json"
DATA_DIR = Path.cwd() / "responses"

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(DATA_DIR / SOURCE_FILE, "r") as json_file:
    saved_response = json.load(json_file)
    image_data = b64decode(saved_response["data"][0]["b64_json"])

response = openai.Image.create_variation(
    image=image_data,
    n=3,
    size="256x256",
    response_format="b64_json",
)

new_file_name = f"vary-{SOURCE_FILE[:4]}-{response['created']}.json"

with open(DATA_DIR / new_file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)
