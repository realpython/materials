def average_grade(grades):
    if len(grades) == 0:
        raise ValueError("empty grades not allowed")
    return sum(grades) / len(grades)
