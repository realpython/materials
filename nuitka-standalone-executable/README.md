# Nuitka: Compile Your Python Code Into a Standalone Executable

Sample code for the Real Python tutorial on compiling Python applications with Nuitka.

## Files

- `wordcount.py`: A small command-line tool that counts the most common words in a text file
- `sample.txt`: Sample text used to test `wordcount.py`
- `cpu_benchmark.py`: A CPU-bound benchmark script used to compare runtime performance across regular Python, `--mode=standalone`, and `--mode=onefile` builds

## Usage

Install Nuitka:

```console
$ python -m pip install nuitka
```

Compile `wordcount.py`:

```console
$ python -m nuitka --mode=standalone wordcount.py
```

Run the compiled executable against `sample.txt`:

```console
$ ./wordcount.dist/wordcount sample.txt -n 5
```
