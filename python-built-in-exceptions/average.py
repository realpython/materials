def average_grade(grades):
    if not grades:
        raise ValueError("empty grades not allowed")
    return sum(grades) / len(grades)
