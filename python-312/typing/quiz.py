import pathlib
import random
from dataclasses import dataclass
from string import ascii_lowercase
from typing import Self, override


@dataclass
class Question:
    question: str
    answer: str

    @classmethod
    def from_file(cls, path: pathlib.Path) -> Self:
        question, answer, *_ = path.read_text(encoding="utf-8").split("\n")
        return cls(question, answer)

    def ask(self) -> bool:
        answer = input(f"\n{self.question} ")
        return answer == self.answer


@dataclass
class MultipleChoiceQuestion(Question):
    distractors: list[str]

    @classmethod
    @override
    def from_file(cls, path: pathlib.Path) -> Self:
        question, answer, *distractors = (
            path.read_text(encoding="utf-8").strip().split("\n")
        )
        return cls(question, answer, distractors)

    @override
    def ask(self) -> bool:
        print(f"\n{self.question}")

        alternatives = random.sample(
            self.distractors + [self.answer], k=len(self.distractors) + 1
        )
        labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
        for label, alternative in labeled_alternatives.items():
            print(f"   {label}) {alternative}", end="")

        answer = input("\n\nChoice? ")
        return labeled_alternatives.get(answer) == self.answer


questions = [
    Question("Who created Python?", "Guido van Rossum"),
    MultipleChoiceQuestion(
        "What's a PEP?",
        "A Python Enhancement Proposal",
        distractors=[
            "A Pretty Exciting Policy",
            "A Preciously Evolved Python",
            "A Potentially Epic Prize",
        ],
    ),
    MultipleChoiceQuestion.from_file(pathlib.Path("oslo.question")),
]

score = 0
for question in random.sample(questions, k=len(questions)):
    if question.ask():
        score += 1
        print("Yes, that's correct!")
    else:
        print(f"No, the answer is '{question.answer}'")

print(f"\nYou got {score} out of {len(questions)} correct")
