from base64 import b64decode

from openai import OpenAI

client = OpenAI()

PROMPT = "A vaporwave computer"

response = client.images.generate(
    model="gpt-image-2",
    prompt=PROMPT,
    n=1,
    size="1024x1024",
    quality="low",
)

with open("vaporwave.png", mode="wb") as png:
    png.write(b64decode(response.data[0].b64_json))
