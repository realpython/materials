# Use case 1: If the student fails 2 or more tests, the student must go to tutoring (for-loop)
scores = [90, 30, 50, 70, 85, 35]

num_failed_scores = 0
failed_score = 60
needs_utoring = False
for score in scores:
    if score < failed_score:
        num_failed_scores += 1
    if num_failed_scores >= 2:
        needs_tutoring = True
        break

print("Does the student need tutoring? " + str(needs_tutoring))
