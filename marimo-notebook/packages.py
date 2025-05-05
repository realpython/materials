# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "pandas==2.2.3",
# ]
# ///
import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    data = {"rank": [1, 2, 3], "language": ["Python", "Java", "JavaScript"]}
    languages = pd.DataFrame(data)

    languages

    return data, languages, pd


if __name__ == "__main__":
    app.run()
