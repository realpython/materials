import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781",
        "1771",
        "1871",
        "1881",
    ],
    "Which built-in function can get information from the user": [
        "input",
        "get",
        "print",
        "write",
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for",
        "while",
        "each",
        "loop",
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort",
        "Quicksort",
        "Merge sort",
        "Bubble sort",
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None",
        "key",
        "True",
        "False",
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ],
}


def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


if __name__ == "__main__":
    run_quiz()
