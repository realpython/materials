SUBJECT_TEMPLATE = "{name:<15} Grade: {grade:3} Comment: {comment}"
REPORT_TEMPLATE = """
Progress Report. Student: {name}
Average: {average:.2f} / 100

Course Details:
{subjects_report}

Thank you for reviewing the progress report.
"""

student = {
    "name": "John Doe",
    "subjects": [
        {
            "name": "Mathematics",
            "grade": 88,
            "comment": "Excellent improvement.",
        },
        {
            "name": "Science",
            "grade": 92,
            "comment": "Outstanding performance.",
        },
        {
            "name": "History",
            "grade": 78,
            "comment": "Needs to participate more.",
        },
        {"name": "Art", "grade": 85, "comment": "Very creative."},
    ],
}


def build_student_report(student):
    data = {
        "name": student["name"],
        "average": sum(subject["grade"] for subject in student["subjects"])
        / len(student["subjects"]),
        "subjects_report": "\n".join(
            SUBJECT_TEMPLATE.format(**subject)
            for subject in student["subjects"]
        ),
    }

    return REPORT_TEMPLATE.format(**data)


print(build_student_report(student))
