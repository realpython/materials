"""Calculate student grades by combining data from many sources.

Using Pandas, this script combines data from the:

* Roster
* Homework & Exam grades
* Quiz grades

to calculate final grades for a class.
"""
from pathlib import Path
import pandas as pd
import numpy as np

HERE = Path(__file__).parent
DATA_FOLDER = HERE.parent / "data"

roster = pd.read_csv(
    DATA_FOLDER / "roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

hw_exam_grades = pd.read_csv(
    DATA_FOLDER / "hw_exam_grades.csv",
    converters={"SID": str.lower, "Email Address": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID",
)

quiz_grades = pd.DataFrame()
for f in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = " ".join(f.stem.title().split("_")[:2])
    quiz = pd.read_csv(
        f,
        converters={"Email": str.lower},
        index_col=["Email"],
        usecols=["Email", "Grade"],
    ).rename(columns={"Grade": quiz_name})
    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)

final_data = pd.merge(
    roster, hw_exam_grades, left_index=True, right_index=True,
)

final_data = pd.merge(
    final_data, quiz_grades, left_on="Email Address", right_index=True
)

final_data = final_data.fillna(0)

n_exams = 3
for n in range(1, n_exams + 1):
    final_data[f"Exam {n} Score"] = (
        final_data[f"Exam {n}"] / final_data[f"Exam {n} - Max Points"]
    )

homework_scores = final_data.filter(regex=r"^Homework \d\d?$", axis=1)
homework_max_points = final_data.filter(regex=r"^Homework \d\d? -", axis=1)

# print(homework_scores.to_markdown())

sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max

# print(
#     sum_of_hw_scores.to_markdown(),
#     sum_of_hw_max.to_markdown(),
#     final_data["Total Homework"].to_markdown(),
# )

hw_max_renamed = homework_max_points.set_axis(homework_scores.columns, axis=1)
overall_hw_scores = (homework_scores / hw_max_renamed).sum(axis=1)
final_data["Overall Homework"] = overall_hw_scores / homework_scores.shape[1]

# print(
#     overall_hw_scores.to_markdown(),
#     final_data["Overall Homework"].to_markdown(),
# )

final_data["Homework Score"] = final_data[
    ["Total Homework", "Overall Homework"]
].max(axis=1)


quiz_scores = final_data.filter(regex=r"^Quiz \d$", axis=1)
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 16, "Quiz 4": 16, "Quiz 5": 11}
)

sum_of_quiz_scores = quiz_scores.sum(axis=1)
sum_of_quiz_max = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_hw_scores / sum_of_hw_max

overall_quiz_scores = (quiz_scores / quiz_max_points).sum(axis=1)
final_data["Overall Quizzes"] = overall_quiz_scores / quiz_scores.shape[1]

final_data["Quiz Score"] = final_data[
    ["Total Quizzes", "Overall Quizzes"]
].max(axis=1)

weightings = pd.Series(
    {
        "Exam 1 Score": 0.05,
        "Exam 2 Score": 0.1,
        "Exam 3 Score": 0.15,
        "Quiz Score": 0.30,
        "Homework Score": 0.4,
    }
)

final_data["Final Score"] = (final_data[weightings.index] * weightings).sum(
    axis=1
)
final_data["Ceiling Score"] = np.ceil(final_data["Final Score"] * 100)

# print(final_data[["Final Score", "Ceiling Score"]].to_markdown())

grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}


def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter


letter_grades = final_data["Ceiling Score"].map(grade_mapping)
final_data["Final Grade"] = pd.Categorical(
    letter_grades, categories=grades.values(), ordered=True
)
print(final_data["Final Grade"].to_markdown())
