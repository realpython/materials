# Pandas Project: Make a Gradebook With Pandas

The code in this folder is used to generate and process the data for the tutorial [_Pandas Project: Make a Gradebook With Pandas_](https://realpython.com/pandas-project-gradebook).

## `generate_data.py`

The script `generate_data.py` uses the [Faker](https://faker.readthedocs.io/en/master/) library to generate fake student names and NumPy to generate scores for homework, exams, and quizzes. The data are stored as CSV files in the `data` folder. With the seed that is set in the script, the data used in the article can be reproduced. To try out new data, change the seed for the NumPy random number generator.

## Folders with `gradebook.py` Scripts

In the article, you create a script called `gradebook.py`. For didactic purposes, each of the steps in the development process is broken into a separate folder here. The `gradebook.py` scripts build from one folder to the next, to generate the final copy in the root directory here. The order in the article is:

1. `loading-the-data`
2. `merging-dataframes`
3. `calculating-grades`
4. `grouping-the-data`
5. `plotting-summary-statistics`

## Installing Dependencies

There are two `requirements.txt`-style files in this repository. The `generate_data-reqs.txt` contains the dependencies for the `generate_data.py` script. The `gradebook-reqs.txt` file contains the dependencies for the `gradebook.py` script.
