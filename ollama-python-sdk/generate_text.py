from ollama import generate

response = generate(
    model="llama3.2:latest",
    prompt="Explain what Python is in one sentence.",
)

print(response.response)
