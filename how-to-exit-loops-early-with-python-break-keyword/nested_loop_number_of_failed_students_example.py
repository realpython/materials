scores = [[90, 30, 80, 100], [100, 80, 95, 87], [75, 84, 77, 90]]

failed_score = 60
num_failed_students = 0
for student_score_list in scores:
    for score in student_score_list:
        if score < failed_score:
            num_failed_students += 1
            break
print("Number of students who failed a test: " + str(num_failed_students))
