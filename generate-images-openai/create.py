import json
from pathlib import Path

from openai import OpenAI

client = OpenAI()

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

response = client.images.generate(
    model="gpt-image-2",
    prompt=PROMPT,
    n=1,
    size="1024x1024",
    quality="low",
)

file_name = DATA_DIR / f"{PROMPT[:5]}-{response.created}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response.to_dict(), file)
