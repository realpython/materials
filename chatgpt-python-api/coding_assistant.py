from openai import OpenAI

user_input = input("How can I help you? ")

client = OpenAI()

code_response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "developer",
            "content": (
                "You are a Python coding assistant. "
                "Only accept Python related questions."
            ),
        },
        {
            "role": "user",
            "content": f"{user_input}",
        },
    ],
)

print(f"\n{code_response.output_text}")
