# Use case 1: If the student fails 2 or more tests, the student must go to tutoring (for loop)
scores = [90, 30, 50, 70, 85, 35]

numFailedScores = 0
failedScore = 60
needsTutoring = False
for score in scores:
    if score < failedScore:
        numFailedScores += 1
    if numFailedScores >= 2:
        needsTutoring = True
        break

print("Does the student need tutoring? " + str(needsTutoring))
