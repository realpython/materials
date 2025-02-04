# Use case 2: Print out the score of the first five tests (while loop)
scores = [90, 30, 50]
i = 0

while i < 5:
    if i > len(scores) - 1:
        # If there are less than 5 scores, break out of the loop when all scores are printed
        break
    print("Score: " + str(scores[i]))
    i += 1
