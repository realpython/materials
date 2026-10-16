from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[{"role": "user", "content": "What's in the habits folder?"}],
)

print(response.choices[0].message.content)
