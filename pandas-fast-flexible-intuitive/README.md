# Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects

Corresponding data for ["Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects."](https://realpython.com/fast-flexible-pandas/)

## Running the Script

Install the pinned dependencies first:

```bash
$ python -m pip install -r requirements.txt
```

The module `tutorial/__main__.py` is the script that mimics the tutorial code.  A `__main__.py` script has the effect of executing when the containing package is run as `python -m <packagename>`.

Here is an example output (Python 3.14, pandas 3.0.6):

```bash
 pandas-fast-flexible-intuitive$ python3 -m tutorial
Companion code to https://realpython.com/fast-flexible-pandas.

'Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects'

Note: most of the functions here modify a Pandas DataFrame in-place,
which is generally not great practice but used with caution here.

Python version: 3.14.6
Pandas version: 3.0.6

Timing code ...

Best of 3 trials with 10 function calls per trial:
Function `convert` ran in average of 0.374 seconds.

Best of 3 trials with 100 function calls per trial:
Function `convert_with_format` ran in average of 0.018 seconds.

Best of 2 trials with 10 function calls per trial:
Function `apply_tariff_loop` ran in average of 1.338 seconds.

Best of 3 trials with 50 function calls per trial:
Function `apply_tariff_iterrows` ran in average of 0.326 seconds.

Best of 3 trials with 100 function calls per trial:
Function `apply_tariff_withapply` ran in average of 0.067 seconds.

Best of 3 trials with 1000 function calls per trial:
Function `apply_tariff_isin` ran in average of 0.003 seconds.

Best of 3 trials with 1000 function calls per trial:
Function `apply_tariff_cut` ran in average of 0.001 seconds.

Best of 3 trials with 1000 function calls per trial:
Function `apply_tariff_digitize` ran in average of 0.000 seconds.
```
