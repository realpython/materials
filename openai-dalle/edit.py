import json
import os
from pathlib import Path

import openai

SOURCE_PATH = Path.cwd() / "images" / "An ec-1667994848"
DESTINATION_PATH = Path.cwd() / "responses"
PROMPT = "A 90s vaporwave computer showing Rick Astley on the screen"

SOURCE_PATH.mkdir(parents=True, exist_ok=True)
DESTINATION_PATH.mkdir(parents=True, exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create_edit(
    image=open(SOURCE_PATH / "computer.png", "rb"),
    mask=open(SOURCE_PATH / "mask.png", "rb"),
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

with open(
    DESTINATION_PATH / f"edit-{PROMPT[:5]}-{response['created']}.json",
    mode="w",
) as fp:
    json.dump(response, fp)
