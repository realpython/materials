WORD = "SNAKE"

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == WORD:
        print("Correct")
        break

    correct_letters = {
        letter for letter, correct in zip(guess, WORD) if letter == correct
    }
    misplaced_letters = set(guess) & set(WORD) - correct_letters
    wrong_letters = set(guess) - set(WORD)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))
