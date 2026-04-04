import anthropic

client = anthropic.Anthropic()

system_prompt = """
You are a Python coding assistant. You only answer questions about Python.
If the user asks about any other programming language or unrelated topic,
politely explain that you can only help with Python questions.
"""

user_input = input("Ask me anything about Python: ")

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {"role": "user", "content": user_input}
    ],
)

print(f"\n{response.content[0].text}")
