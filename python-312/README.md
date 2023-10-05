# Python 3.12 Demos

This repository holds example code that demos some of the new features in Python 3.12.

## Introduction

You need Python 3.12 installed to run these examples. See the following tutorial instructions:

- [How Can You Install a Pre-Release Version of Python](https://realpython.com/python-pre-release/)

Note that for the `perf` support, you'll need to build Python from source code with additional compiler flags enabled, as [explained below](#support-for-the-linux-perf-profiler).

You can learn more about Python 3.12's new features in the following Real Python tutorials:

- [Python 3.12: Cool New Features for You to Try](https://realpython.com/python312-new-features/)
- [Python 3.12 Preview: Ever Better Error Messages](https://realpython.com/python312-error-messages/)
- [Python 3.12 Preview: Support For the Linux `perf` Profiler](https://realpython.com/python312-perf-profiler/)
- [Python 3.12 Preview: More Intuitive and Consistent F-Strings](https://realpython.com/python312-f-strings/)
- [Python 3.12 Preview: Subinterpreters](https://realpython.com/python312-subinterpreters/)
- [Python 3.12 Preview: Static Typing Improvements](https://realpython.com/python312-typing/)

You'll find examples from these tutorials in this repository.

## Examples

This section only contains brief instructions on how you can run the examples. See the tutorials for technical details.

### Improved Error Messages

Run [`encoder.py`](error-messages/encoder.py) to create an encoded message like the one shown in the tutorial. You can decode the message using [`decoder.py`](error-messages/decoder.py).

You can swap the import statement to `import d from this` in either of the files to encounter the improved error message:

```python
>>> import d from this
  File "<stdin>", line 1
    import d from this
    ^^^^^^^^^^^^^^^^^^
SyntaxError: Did you mean to use 'from ... import ...' instead?
```

In [`local_self.py`](error-messages/local_self.py), you can see a naive reproduction of another improved error message. Pick apart the example code to learn more about how this was implemented in Python 3.12. You can also run [`shapes.py`](error-messages/shapes.py) to see the _self_ error message in action.

See [Ever Better Error Messages in Python 3.12](https://realpython.com/python312-error-messages/) for more information.

### Support For the Linux `perf` Profiler

#### Setting Up

You'll need to download, build, and install Python 3.12 from the source code with the frame pointer optimizations disabled:

```shell
$ git clone --branch v3.12.0b2 https://github.com/python/cpython.git
$ cd cpython/
$ export CFLAGS='-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer'
$ ./configure --prefix="$HOME/python-custom-build"
$ make -j $(nproc)
$ make install
```

Create and activate a new virtual environment based on Python 3.12:

```shell
$ "$HOME/python-custom-build/bin/python3" -m venv venv/ --prompt 'py3.12-custom'
$ source venv/bin/activate
```

Install dependencies from the `requirements.txt` file into your virtual environment:

```shell
(py3.12-custom) $ python -m pip install -r requirements.txt
```

#### Using `perf` With Python

Record Samples:

```shell
$ cd perf-profiler/
$ sudo perf record -g -F max ../venv/bin/python -X perf benchmark.py
```

Display reports:

```shell
$ cd perf-profiler/
$ sudo perf report
$ sudo perf report --stdio -g
$ sudo perf report --hierarchy --verbose --call-graph fractal --sort sample,dso
```

#### Rendering Flame Graphs

Download Perl scripts and add them to your `$PATH` environment variable:

```shell
$ git clone git@github.com:brendangregg/FlameGraph.git
$ export PATH="$(pwd)/FlameGraph:$PATH"
```

Generate the flame graph and save it to a local file:

```shell
$ cd perf-profiler/
$ sudo perf script | stackcollapse-perf.pl | flamegraph.pl > flamegraph.svg
```

Open the flame graph in your default SVG viewer: (Use your web browser for the interactive features.)

```shell
$ xdg-open flamegraph.svg
```

Produce a pure-Python flame graph by filtering and processing the collapsed stack traces:

```shell
$ sudo perf script | stackcollapse-perf.pl > traces.txt
$ cat traces.txt | python censor.py -m benchmark,PIL > traces_censored.txt
$ cat traces_censored.txt | flamegraph.pl --minwidth 10 > flamegraph.svg
```

See [Support For the Linux `perf` Profiler in Python 3.12](https://realpython.com/python312-perf-profiler/) for more information.

### New F-String Implementation and Syntax Formalization

Once you have 3.12 installed, open any file from the `f-string/` folder. Uncomment the code as needed. [Run the scripts](https://realpython.com/run-python-scripts/) from your command line or execute the code directly in a [REPL](https://realpython.com/python-repl/) session. You'll see the new f-string implementation in action.

For example, go ahead and run the following command:

```console
$ python backslashes.py
Hello
World!
I
am
a
Pythonista!
```

In this example, you can see how the new implementation of f-strings allows you to include backslashes in embedded expressions. This wasn't possible with f-strings in earlier versions of Python. 

### Static Typing Improvements

You'll find all static typing examples inside the [`typing/`](typing/) directory. You should install the Pyright type checker from PyPI:

```console
$ python -m pip install pyright
```

You can then run type checks by running `pyright`. For some features, you need to specify `--pythonversion 3.12`.

#### Type Variables and Generic Classes, Functions, and Type Aliases

You can find comparisons between the old and the new syntax for type variables in the following files, with the new 3.12 syntax shown in the commented part of the code:

- [`generic_queue.py`](typing/generic_queue.py)
- [`generic_stack.py`](typing/generic_stack.py)
- [`list_helpers.py`](typing/list_helpers.py)
- [`concatenation.py`](typing/concatenation.py)
- [`inspect_string.py`](typing/inspect_string.py)
- [`deck.py`](typing/deck.py)
- [`alias.py`](typing/alias.py)

Additionally, [`typed_queue.py`](typing/typed_queue.py) shows the implementation of typed queues without using type variables.

#### Modeling Inheritance With `@override`

The file [`quiz.py`](typing/quiz.py) shows how to use the new `@override` decorator. In addition to the code in the tutorial, this file includes support for reading questions from files. This is done to show that `@override` works well together with other decorators like `@classmethod`.

Similarly, [`accounts.py`](typing/accounts.py) contains the bank account classes annotated with `@override`. To play with the bank account code, you should run it interactively: `python -i accounts.py`.

#### Annotating `**kwargs` With Typed Dictionaries

The file [`options.py`](typing/options.py) shows how you can use a typed dictionary to annotate variable keyword arguments.

### Inlined Comprehensions

You can run benchmarks on comprehensions by running [`comprehension_benchmark.py`](comprehension_benchmark.py). If you have multiple versions of Python, then you should run the benchmarks on all of them and compare the results.

### Group Iterables Into Batches With `itertools.batched()`

Run [`quarters.py`](quarters.py) for an example showing how to group months into quarters.

### List Files and Directories With `Path.walk()`

Run [`pathlib_walk.py`](pathlib_walk.py) to compare `.walk()` and `.rglob()` for listing files and directories.

## Authors

- **Martin Breuss**, E-mail: [martin@realpython.com](martin@realpython.com)
- **Bartosz Zaczyński**, E-mail: [bartosz@realpython.com](bartosz@realpython.com)
- **Leodanis Pozo Ramos**, E-mail: [leodanis@realpython.com](leodanis@realpython.com)
- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
