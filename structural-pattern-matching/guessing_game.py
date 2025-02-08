import random

MIN, MAX = 1, 100
MAX_TRIES = 5
PROMPT_1 = f"\N{mage} Guess a number between {MIN} and {MAX}: "
PROMPT_2 = "\N{mage} Try again: "
BYE = "Bye \N{waving hand sign}"


def main():
    print("Welcome to the game! Type 'q' or 'quit' to exit.")
    while True:
        play_game()
        if not want_again():
            bye()


def play_game():
    drawn_number = random.randint(MIN, MAX)
    num_tries = MAX_TRIES
    prompt = PROMPT_1
    while num_tries > 0:
        match input(prompt):
            case command if command.lower() in ("q", "quit"):
                bye()
            case user_input:
                try:
                    user_number = int(user_input)
                except ValueError:
                    print("That's not a number!")
                else:
                    match user_number:
                        case number if number < drawn_number:
                            num_tries -= 1
                            prompt = PROMPT_2
                            print(f"Too low! {num_tries} tries left.")
                        case number if number > drawn_number:
                            num_tries -= 1
                            prompt = PROMPT_2
                            print(f"Too high! {num_tries} tries left.")
                        case _:
                            print("You won \N{party popper}")
                            return
    print("You lost \N{pensive face}")


def want_again():
    while True:
        match input("Do you want to play again? [Y/N] ").lower():
            case "y":
                return True
            case "n":
                return False


def bye():
    print(BYE)
    exit()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        bye()
