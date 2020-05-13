# Pandas Project: Make a Gradebook With Pandas

The code in this folder is used to generate and process the data for the tutorial [Pandas Project: Make a Gradebook With Pandas_](https://realpython.com/pandas-project-gradebook).

## `generate_data.py`

The script `generate_data.py` uses the [Faker](https://faker.readthedocs.io/en/master/) library to generate fake student names and NumPy to generate scores for homework, exams, and quizzes. The data are stored as CSV files in the `data` folder. With the seed that is set in the script, the data used in the article can be reproduced. To try out new data, change the seed for the NumPy random number generator.

## Numbered Python Scripts

In the article, you create a script called `gradebook.py`. For didactic purposes, each of the steps in the development process is broken into a separate script here. The `.py` scripts build from one example to the next, to generate the final copy called `06-final-gradebook.py`. The order in the article is:

1. `01-loading-the-data.py`
2. `02-merging-dataframes.py`
3. `03-calculating-grades.py`
4. `04-grouping-the-data.py`
5. `05-plotting-summary-statistics.py`

## Installing Dependencies

There are two `requirements.txt` files in this repository. The `data/requirements.txt` contains the dependencies for the `generate_data.py` script. The `requirements.txt` file in the root folder contains the dependencies for the `gradebook.py` script.
