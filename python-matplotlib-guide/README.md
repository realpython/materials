# Python Plotting With Matplotlib (Guide)

This folder provides the code examples for the Real Python tutorial [Python Plotting With Matplotlib (Guide)](https://realpython.com/python-matplotlib-guide/).

The tutorial works through its examples in the REPL. Here, each section of the tutorial is collected into a script you can run end to end, so you can see every result at once and then change the code to see what happens. Lines that the tutorial shows as REPL output are wrapped in `print()` calls, and the canonical `import matplotlib.pyplot as plt` plus `np.random.seed(444)` from the tutorial's opening sit at the top of each script that needs them.

## Setup

Create and activate a virtual environment, then install the requirements:

```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

`requirements.txt` pins the versions the tutorial's examples were verified against. Newer releases will usually work too, but matplotlib changes the repr of its objects and the list of bundled style sheets between releases, so output from other versions won't match the tutorial exactly.

## Usage

After creating and activating your virtual environment, and installing the dependencies, you should be able to run each individual file normally:

```bash
(venv) $ python subplots_notation.py
```

Each script prints its results to the terminal and opens a Matplotlib window for each figure it builds — close each window to move on to the next.

| File | Tutorial section |
| --- | --- |
| `object_hierarchy.py` | The Matplotlib Object Hierarchy |
| `subplots_notation.py` | Understanding `plt.subplots()` Notation |
| `gridspec_housing.py` | Understanding `plt.subplots()` Notation (the `subplot2grid()` and California housing examples) |
| `figures_behind_the_scenes.py` | The "Figures" Behind The Scenes |
| `imshow_and_matshow.py` | A Burst of Color: `imshow()` and `matshow()` |
| `plotting_in_pandas.py` | Plotting in Pandas |
| `appendix_a_configuration.py` | Appendix A: Configuration and Styling |
| `appendix_b_interactive_mode.py` | Appendix B: Interactive Mode |

Two of the scripts download their data at runtime, so they need an internet connection: `gridspec_housing.py` pulls the California housing archive from figshare, and `plotting_in_pandas.py` pulls the CBOE VIX series from FRED.

A few results can't match the tutorial byte for byte. The `id()` values in `figures_behind_the_scenes.py` are memory addresses, so only the comparisons between them are meaningful. And `appendix_b_interactive_mode.py` first prints `False` rather than the tutorial's `True`, because matplotlib starts a script with interactive mode off, while the tutorial's session already had it on.

Two code blocks in the tutorial aren't shipped here, because there's nothing for you to run: the single-line canonical imports in "Pylab: What Is It, and Should I Use It?", and the abridged excerpt of matplotlib's own `pyplot.py` source in "Stateful Versus Stateless Approaches".

You can find more information and context on the code in [Python Plotting With Matplotlib (Guide)](https://realpython.com/python-matplotlib-guide/).
