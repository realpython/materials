from openai import OpenAI

client = OpenAI()
MODEL = "gpt-6-luna"


def trace(sender, receiver, text):
    print(f"  [{sender} -> {receiver}] {text}")


while True:
    user_input = input("you -> harness: ")
    messages = [{"role": "user", "content": user_input}]

    trace("harness", "model", "sending a message")
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    reply = response.choices[0].message
    trace("model", "harness", f"text reply ({len(reply.content)} characters)")

    print(f"harness -> you: {reply.content}")
