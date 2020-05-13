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
DATA_FOLDER = HERE / "data"

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

# print(
#     final_data.loc[
#         ["wxb12345", "mxl12345", "txj12345", "jgf12345"],
#         [f"Exam {n} Score" for n in range(1, n_exams + 1)],
#     ].to_markdown()
# )

homework_scores = final_data.filter(regex=r"^Homework \d\d?$", axis=1)
homework_max_points = final_data.filter(regex=r"^Homework \d\d? -", axis=1)

sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max

# print(
#     pd.concat(
#         [sum_of_hw_scores, sum_of_hw_max, final_data["Total Homework"]], axis=1
#     )
#     .set_axis(
#         ["Sum of Homework Scores", "Sum of Max Scores", "Total Homework"],
#         axis=1,
#     )
#     .loc[["wxb12345", "mxl12345", "txj12345", "jgf12345"]]
#     .to_markdown()
# )

hw_max_renamed = homework_max_points.set_axis(homework_scores.columns, axis=1)
average_hw_scores = (homework_scores / hw_max_renamed).sum(axis=1)
final_data["Average Homework"] = average_hw_scores / homework_scores.shape[1]

# print(
#     pd.concat([average_hw_scores, final_data["Average Homework"]], axis=1)
#     .set_axis(["Sum of Average Homework Scores", "Average Homework"], axis=1)
#     .loc[["wxb12345", "mxl12345", "txj12345", "jgf12345"]]
#     .to_markdown()
# )

final_data["Homework Score"] = final_data[
    ["Total Homework", "Average Homework"]
].max(axis=1)

# print(
#     final_data.loc[
#         ["wxb12345", "mxl12345", "txj12345", "jgf12345"],
#         ["Total Homework", "Average Homework", "Homework Score"],
#     ].to_markdown()
# )

quiz_scores = final_data.filter(regex=r"^Quiz \d$", axis=1)
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
)

sum_of_quiz_scores = quiz_scores.sum(axis=1)
sum_of_quiz_max = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_hw_scores / sum_of_hw_max

average_quiz_scores = (quiz_scores / quiz_max_points).sum(axis=1)
final_data["Average Quizzes"] = average_quiz_scores / quiz_scores.shape[1]

final_data["Quiz Score"] = final_data[
    ["Total Quizzes", "Average Quizzes"]
].max(axis=1)

# print(
#     final_data.loc[
#         ["wxb12345", "mxl12345", "txj12345", "jgf12345"],
#         ["Total Quizzes", "Average Quizzes", "Quiz Score"],
#     ].to_markdown()
# )

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

# print(
#     final_data.loc[
#         ["wxb12345", "mxl12345", "txj12345", "jgf12345"],
#         ["Final Score", "Ceiling Score"],
#     ].to_markdown()
# )

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

# print(
#     final_data.loc[
#         ["wxb12345", "mxl12345", "txj12345", "jgf12345"], ["Final Grade"],
#     ].to_markdown()
# )
