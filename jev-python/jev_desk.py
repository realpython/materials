import os
from pprint import pprint

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api",
)

QUESTIONS = {
    "desk": Choice(
        instructions="Where should the info desk send the visitor?",
        criteria={
            "ticket_counter": "Buying, changing, or refunding tickets.",
            "lost_and_found": "Looking for something they lost.",
            "immediate_help": "An emergency, an injury, or a missing person.",
        },
    ),
    "urgency": Score(
        instructions="How urgent is the request of the visitor?",
        criteria=[
            "Not urgent at all.",
            "Should be handled today.",
            "Should be handled within the next few minutes.",
            "Needs to be handled right now.",
        ],
    ),
    "needs_assistance": Noul(
        instructions=(
            "Does the visitor need a staff member to help them get around "
            "the station, for example because of a wheelchair, heavy "
            "luggage, or small children?"
        ),
    ),
}


def main():
    visitor_says = input("What does the visitor say? ")
    r = client.system_one(
        state={"visitor_says": visitor_says},
        questions=QUESTIONS,
    )
    pprint(r.model_dump()["answers"])


if __name__ == "__main__":
    main()
