"""Calculate student grades by combining data from many sources.

Using Pandas, this script combines data from the:

* Roster
* Homework & Exam grades
* Quiz grades

to calculate final grades for a class.
"""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
DATA_FOLDER = HERE.parent / "data"

roster = pd.read_csv(
    DATA_FOLDER / "roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
)
# print(roster.to_markdown())

hw_exam_grades = pd.read_csv(
    DATA_FOLDER / "hw_exam_grades.csv",
    converters={"SID": str.lower, "Email Address": str.lower},
    usecols=lambda x: "Submission" not in x,
)
# print(hw_exam_grades.to_markdown())

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

print(quiz_grades.to_markdown())
