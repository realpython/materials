# Python Statistics Fundamentals: How to Describe Your Data

This folder contains supplementary code for the Real Python tutorial on [descriptive statistics in Python](https://realpython.com/python-statistics/). You can run the examples as they are, or continue your learning by experimenting with them on your own data.

The tutorial works through the examples in the REPL. Here, each section of the tutorial is collected into a script you can run end to end, so you can see every result at once and then change the numbers to see what happens.

## Setup

Create and activate a virtual environment, then install the requirements:

```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt -c constraints.txt
```

The tutorial's examples were verified against the versions pinned in `constraints.txt`. Newer releases will usually work too, but NumPy 2 changed how scalars are displayed, so output from older versions won't match the tutorial exactly.

## Usage

After creating and activating your virtual environment, and installing the dependencies, you should be able to run each individual file normally:

```bash
(venv) $ python central_tendency.py
```

The statistics scripts print their results to the terminal. The plotting scripts open a Matplotlib window instead, one per figure — close each window to move on to the next.

| File | Tutorial section |
| --- | --- |
| `datasets.py` | The example data every other script imports |
| `central_tendency.py` | Measures of Central Tendency |
| `variability.py` | Measures of Variability |
| `summary_statistics.py` | Summary of Descriptive Statistics |
| `correlation.py` | Measures of Correlation Between Pairs of Data |
| `two_dimensional_data.py` | Working With 2D Data: Axes |
| `dataframes.py` | Working With 2D Data: DataFrames |
| `plot_box.py` | Visualizing Data: Box Plots |
| `plot_histogram.py` | Visualizing Data: Histograms |
| `plot_pie.py` | Visualizing Data: Pie Charts |
| `plot_bar.py` | Visualizing Data: Bar Charts |
| `plot_xy.py` | Visualizing Data: X-Y Plots |
| `plot_heatmap.py` | Visualizing Data: Heatmaps |

Each script is organized into functions named after the statistic they calculate, and running a file calls them in the order the tutorial introduces them. To work with just one measure, import it instead:

```pycon
>>> from central_tendency import harmonic_mean
>>> harmonic_mean()
```

The example data lives in `datasets.py`, so you can swap in your own numbers in one place and re-run any script against them.

You can find more information and context on the code in [Python Statistics Fundamentals: How to Describe Your Data](https://realpython.com/python-statistics/).
