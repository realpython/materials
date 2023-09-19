class GradeValueError(Exception):
    pass


def calculate_average_grade(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            raise GradeValueError(
                "grade values must be between 0 and 100 inclusive"
            )
        total += grade
        count += 1
    return round(total / count, 2)
