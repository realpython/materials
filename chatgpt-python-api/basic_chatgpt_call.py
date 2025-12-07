from openai import OpenAI

client = OpenAI()

text_response = client.responses.create(
    model="gpt-5",
    input="Tell me a joke about Python programming"
)

print(f"Joke:\n{text_response.output_text}")
