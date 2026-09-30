import os

from typesafe_sdk import Noul, TypeSafeClient

client = TypeSafeClient(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api",
)


def respond(lost_something):
    if lost_something:
        print("You can find the lost and found counter on the right.")
    else:
        print("What can I help you with?")


def ask():
    while True:
        answer = input("Did you lose something? ")
        r = client.system_one(
            state=answer,
            questions={
                "lost_something": Noul(
                    instructions="Is the answer from the user affirmative?"
                ),
            },
        )
        lost_something = r.answers["lost_something"].noul
        if lost_something > 0.8:
            return True
        if lost_something < 0.2:
            return False
        print("Sorry, I didn't get that.")


def main():
    lost_something = ask()
    respond(lost_something)


if __name__ == "__main__":
    main()
