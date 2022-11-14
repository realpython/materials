# How to List the Files in a Directory with Python

The code samples and supporting materials for the [corresponding tutorial](https://realpython.com/[PLACEHOLDER]) on Real Python.

You'll find two directories to test your listing operations on:

1. `Desktop`: A few files, and a few subdirectories with a few files
2. `Desktop_large`: A directory with files and subdirectories. Each subdirectory also has subdirectories and files going three levels deep.

The first one is to experiment with the different listing solutions, the second one is mainly for testing performance.

## Bonus Materials

You'll also find a `bonus` folder. Here you'll find scripts that time a whole range of methods from the `pathlib` and `os` modules when it comes to producing a list of files.

Testing all the methods to produce a basic list of files is not a very fair test, because some methods are optimized to be faster for flat listing whereas others perform better at recursive listing. That said, the results are interesting nonetheless.
