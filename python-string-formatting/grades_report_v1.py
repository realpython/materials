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
    report_header = f"Progress Report. Student: {student['name']}"

    total = sum(subject["grade"] for subject in student["subjects"])
    average = total / len(student["subjects"])
    average_report = f"Average: {average:.2f} / 100\n"

    subject_report = "Course Details:\n"
    for subject in student["subjects"]:
        subject_report += (
            f"{subject['name']:<15} "
            f"Grade: {subject['grade']:3d} "
            f"Comment: {subject['comment']}\n"
        )

    return f"""
{report_header}
{average_report}
{subject_report}
Thank you for reviewing the progress report.
    """


print(build_student_report(student))
