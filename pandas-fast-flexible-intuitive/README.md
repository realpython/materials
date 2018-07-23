# Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects

Corresponding data for ["Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects."](https://realpython.com/fast-flexible-pandas/)

## Running the Script

The module `tutorial/__main__.py` is the script that mimics the tutorial code.  A `__main__.py` script has the effect of executing when the containing package is run as `python -m <packagename>`.

Here is an example output (MacBook Pro, 3.1 GHz Intel Core i5):

```bash
 pandas-fast-flexible-intuitive$ python3 -m tutorial
Companion code to https://realpython.com/fast-flexible-pandas.

'Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects'

Note: most of the functions here modify a Pandas DataFrame in-place,
which is generally not great practice but used with caution here.

Python version: 3.6.6
Pandas version: 0.23.2

Timing code ...

Best of 3 trials with 10 function calls per trial:
Function `convert` ran in average of 1.348 seconds.

Best of 3 trials with 100 function calls per trial:
Function `convert_with_format` ran in average of 0.025 seconds.

Best of 2 trials with 10 function calls per trial:
Function `apply_tariff_loop` ran in average of 3.313 seconds.

Best of 3 trials with 50 function calls per trial:
Function `apply_tariff_iterrows` ran in average of 0.650 seconds.

Best of 3 trials with 100 function calls per trial:
Function `apply_tariff_withapply` ran in average of 0.202 seconds.

Best of 3 trials with 1000 function calls per trial:
Function `apply_tariff_isin` ran in average of 0.004 seconds.

Best of 3 trials with 1000 function calls per trial:
Function `apply_tariff_cut` ran in average of 0.001 seconds.

Best of 3 trials with 1000 function calls per trial:
Function `apply_tariff_digitize` ran in average of 0.001 seconds.
```
