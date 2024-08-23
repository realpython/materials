from openai import OpenAI

client = OpenAI()

PROMPT = "A vaporwave computer"


response = client.images.generate(
    model="dall-e-3",
    prompt=PROMPT,
)

print(response.data[0].url)
print(response.data[0].revised_prompt)
