scores = [90, 30, 50, 70, 85, 35]

num_failed_scores = 0
failed_score = 60
needs_tutoring = "No"
for score in scores:
    if score < failed_score:
        num_failed_scores += 1
    if num_failed_scores >= 2:
        needs_tutoring = "Yes"
        break

print(f"Does the student need tutoring? {needs_tutoring}")
