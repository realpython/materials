# Build a Quiz Application With Python

This repository holds the code for the Real Python [Build a Quiz Application With Python](https://realpython.com/python-quiz-application/) tutorial.

The tutorial uses the [walrus operator](https://realpython.com/python-walrus-operator/), which was introduced in [Python 3.8](https://realpython.com/python38-new-features/). The [`source_code_final_37`](source_code_final/) directory shows a quiz application version that doesn't use the walrus operator and runs on [Python 3.7](https://realpython.com/python37-new-features/).

## Dependencies

If you're running on Python 3.10 or earlier, then you need to install [`tomli`](https://pypi.org/project/tomli/) which is used to read TOML data files. You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

You can then install `tomli` with `pip`:

```console
(venv) $ python -m pip install tomli
```

If you're running Python 3.11 or later, then `tomllib` provides TOML support in the standard library. In this case, you don't need to create a virtual environment or install any third-party dependencies.

## Run the Quiz

Enter one of the `source_code_...` folders. You can then run the quiz by running `quiz.py` as a script:

```console
(venv) $ python quiz.py
```

Check out the `questions.toml` file for a list of the questions that are available (in step 4 and later). Edit this file to add your own questions.

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
