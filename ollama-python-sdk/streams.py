from ollama import chat

stream = chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "Explain Python dataclasses with a quick example.",
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.message.content, end="", flush=True)
