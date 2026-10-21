from openai import OpenAI

client = OpenAI()
MODEL = "gpt-6-luna"


def trace(sender, receiver, text):
    print(f"  [{sender} -> {receiver}] {text}")


messages = []

while True:
    user_input = input("you -> harness: ")
    messages.append({"role": "user", "content": user_input})

    trace("harness", "model", f"sending {len(messages)} message(s)")
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    reply = response.choices[0].message
    messages.append(reply)
    trace("model", "harness", f"text reply ({len(reply.content)} characters)")

    print(f"harness -> you: {reply.content}")
