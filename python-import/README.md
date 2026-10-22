# Python `import`: Advanced Techniques and Tips

This folder contains code and materials used in Real Python's [Python `import`: Advanced Techniques and Tips](https://realpython.com/python-import/) article.

The code was tested with Python 3.15.1 and 3.14.9. Install the third-party dependencies with:

```console
$ python -m pip install PyYAML==6.0.3 matplotlib==3.11.2 colorama==0.4.6
```

The `namespace_package/` examples expect `third_party/` and `local/` on your import path, for example by running `sys.path.extend(["third_party", "local"])` from inside that folder, as the tutorial shows. The population examples need the UN data file described in `population_quiz/data/README.md`.
