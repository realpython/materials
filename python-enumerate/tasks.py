tasks_by_priority = ["Pay Rent", "Clean Dishes", "Buy Milk"]

for index, task in enumerate(tasks_by_priority):
    if index == 0:
        print(f"* {task.upper()}!")
    else:
        print(f"* {task}")
