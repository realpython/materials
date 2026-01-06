from ollama import chat

messages = [
    {
        "role": "system",
        "content": "You are an expert Python tutor.",
    },
    {
        "role": "user",
        "content": "Define list comprehensions in a sentence.",
    },
]
response = chat(model="llama3.2:latest", messages=messages)
print(response.message.content)

messages.append(response.message)  # Keep context
messages.append(
    {
        "role": "user",
        "content": "Provide a short, practical example.",
    }
)
response = chat(model="llama3.2:latest", messages=messages)
print(response.message.content)
