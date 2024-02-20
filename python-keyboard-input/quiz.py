questions = {
    "What are the four colors of the Kenyan flag? ": {
        "green",
        "black",
        "red",
        "white",
    },
    "What are the three colors of the French flag? ": {"blue", "red", "white"},
    "How do you spell the first three numbers in Norwegian? ": {
        "en",
        "to",
        "tre",
    },
}

for question, correct in questions.items():
    while True:
        answers = {
            answer.strip().lower() for answer in input(question).split(",")
        }
        if len(answers) == len(correct):
            break
        print(f"Please enter {len(correct)} answers separated by comma")
    if answers == correct:
        print("Correct")
    else:
        print(f"No, the correct answer is {', '.join(correct)}")
