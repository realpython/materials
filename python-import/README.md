# Python `import`: Advanced Techniques and Tips

This folder contains code and materials used in Real Python's [Python `import`: Advanced Techniques and Tips](https://realpython.com/python-import/) article.

The code was tested with Python 3.15.1 and 3.14.9. Install the third-party dependencies with:

```console
$ python -m pip install PyYAML==6.0.3 matplotlib==3.11.2 colorama==0.4.6
```

The examples need Python 3.9 or later, since they use `importlib.resources.files()`.

Some examples need a bit of setup before you run them:

- **`namespace_package/`:** Start Python inside this folder and run `sys.path.extend(["third_party", "local"])` first, as the tutorial shows.
- **`population_quiz/`:** Download the UN data file described in `population_quiz/data/README.md`. Then run `python population_quiz.py` or `python -c "import population"` from inside `population_quiz/`, so that Python finds the `data` package.
- **`structure/`:** Run `python cli.py structure` from inside `structure/`, or install the project with `python -m pip install -e .` from that folder.
