def rock_paper_scissors(choice):
    if choice < 0 or choice > 2:
        raise ValueError("number must be 0, 1, or 2")

    choices = ["rock", "paper", "scissors"]
    return choices[choice]
