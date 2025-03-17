scores = [90, 30, 50, 70, 85, 35]

num_failed_scores = 0
failed_score = 60
for score in scores:
    if score < failed_score:
        num_failed_scores += 1
print(f"Number of failed tests: {num_failed_scores}")
