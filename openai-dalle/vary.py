import json
from base64 import b64decode
from pathlib import Path

from openai import OpenAI

client = OpenAI()

DATA_DIR = Path.cwd() / "responses"
SOURCE_FILE = DATA_DIR / "An ec-1667994848.json"

with open(SOURCE_FILE, mode="r", encoding="utf-8") as json_file:
    saved_response = json.load(json_file)
    image_data = b64decode(saved_response["data"][0]["b64_json"])

response = client.images.create_variation(
    image=image_data,
    n=3,
    size="256x256",
    response_format="b64_json",
)

new_file_name = f"vary-{SOURCE_FILE.stem[:5]}-{response.created}.json"

with open(DATA_DIR / new_file_name, mode="w", encoding="utf-8") as file:
    json.dump(response.to_dict(), file)
