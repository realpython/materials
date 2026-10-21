import argparse
import csv
from functools import cache

import dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

REVIEWS_CSV_PATH = "reviews.csv"


@cache
def load_reviews():
    with open(REVIEWS_CSV_PATH, newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


@tool
def count_reviews(hospital: str) -> str:
    """Count how many patient reviews a specific hospital has.

    Use when asked how many reviews a hospital has. This tool only
    counts reviews per hospital, so it can't count reviews by topic,
    such as how many patients complained about something. Pass only
    the hospital name. For instance, if the question is "How many
    reviews does Wallace-Hamilton have?", the input should be
    "Wallace-Hamilton".
    """
    count = sum(
        row["hospital_name"].lower() == hospital.strip().lower()
        for row in load_reviews()
    )
    if count:
        return f"{hospital} has {count} reviews"
    return f"No reviews found for {hospital}"


@tool
def find_physician_hospitals(physician: str) -> str:
    """Find the hospitals where a physician has patient reviews.

    Use when asked where a physician works or which hospitals a
    physician is associated with. Pass only the physician's full name.
    For instance, if the question is "Where does Dr. Laura Brown
    work?", the input should be "Laura Brown".
    """
    hospitals = sorted(
        {
            row["hospital_name"]
            for row in load_reviews()
            if row["physician_name"].lower() == physician.strip().lower()
        }
    )
    if hospitals:
        return f"{physician} has reviews at: {', '.join(hospitals)}"
    return f"No reviews found for {physician}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    args = parser.parse_args()

    dotenv.load_dotenv()
    agent = create_agent(
        model=ChatOpenAI(model="gpt-6-luna", output_version="responses/v1"),
        tools=[count_reviews, find_physician_hospitals],
        system_prompt=(
            "Answer questions about hospital reviews with your tools."
        ),
    )
    response = agent.invoke(
        {"messages": [{"role": "user", "content": args.question}]}
    )
    print(response["messages"][-1].text)


if __name__ == "__main__":
    main()
