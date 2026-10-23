# /// script
# requires-python = ">=3.11"
# dependencies = ["openai==3.35.1"]
# ///
from openai import OpenAI

client = OpenAI()
MODEL = "gpt-5.4-mini"


SYSTEM = {"role": "system", "content": "Answer in one short sentence."}


def chat(messages):
    response = client.chat.completions.create(
        model=MODEL, messages=[SYSTEM, *messages]
    )
    return response.choices[0].message.content


history = []
for turn in ["Hi, I'm Ana and I'm learning Python.", "What's my name?"]:
    history.append({"role": "user", "content": turn})
    reply = chat(history)  # The whole history goes in every call
    history.append({"role": "assistant", "content": reply})
    print(f"With history:    {reply}")

# Same question, but without the earlier turns
print(
    "Without history:", chat([{"role": "user", "content": "What's my name?"}])
)
