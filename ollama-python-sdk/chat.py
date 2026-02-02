from ollama import chat

messages = [
    {
        "role": "user",
        "content": "Explain what Python is in one sentence.",
    },
]

response = chat(model="llama3.2:latest", messages=messages)
print(response.message.content)
