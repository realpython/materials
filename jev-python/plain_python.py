def respond(lost_something):
    if lost_something:
        print("You can find the lost and found counter on the right.")
    else:
        print("What can I help you with?")


def ask():
    while True:
        answer = input("Did you lose something? (Y/N) ")
        if answer == "Y":
            return True
        if answer == "N":
            return False
        print("Please answer with Y or N.")


def main():
    lost_something = ask()
    respond(lost_something)


if __name__ == "__main__":
    main()
