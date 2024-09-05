import json
from pathlib import Path

from openai import OpenAI

client = OpenAI()

SOURCE_PATH = Path.cwd() / "images" / "An ec-1667994848"
DESTINATION_PATH = Path.cwd() / "responses"
PROMPT = "A 90s vaporwave computer showing Rick Astley on the screen"

SOURCE_PATH.mkdir(parents=True, exist_ok=True)
DESTINATION_PATH.mkdir(parents=True, exist_ok=True)

response = client.images.edit(
    image=open(SOURCE_PATH / "computer.png", mode="rb"),
    mask=open(SOURCE_PATH / "mask.png", mode="rb"),
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

with open(
    DESTINATION_PATH / f"edit-{PROMPT[:5]}-{response.created}.json",
    mode="w",
    encoding="utf-8",
) as file:
    json.dump(response.to_dict(), file)
