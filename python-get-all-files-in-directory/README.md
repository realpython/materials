# How to Get a List of All Files in a Directory With Python

The code samples and supporting materials for the [corresponding tutorial](https://realpython.com/get-all-files-in-directory-python/) on Real Python.

You'll find a directory to test your listing operations on, `Desktop`, which contains a few files, and a few subdirectories with a few files.

You'll also find a script called [`create_large_dir.py`](create_large_dir.py) which will create the `large_dir/` example shown in the tutorial. You can try tweaking the numbers there to bulk up the number of files or create custom directory trees.

You can use these directories to try out the different methods of listing.

The examples covered in the tutorial are in `examples.py`, with the recursive `.iterdir()` function in `skip_dirs.py`.

## Bonus Materials

You'll also find a `bonus` folder. Here you'll find scripts that time a whole range of methods from the `pathlib` and `os` modules when it comes to producing a list of files.

The main testing files are `testing_flat_dir.py` and `testing_nested_dir.py`/. You can tweak the constants at the beginning of these files to change the number of files and/or folders being tested. Along with the number of times the operations are tested. Be warned, though, that bumping up the numbers can cause the tests to take a long time.

These scripts use the `make_files.py` module to generate large flat and nested directories just for the test.

Testing all the methods to produce a basic list of files isn't a very fair test, because some methods are optimized to be faster for flat listing, whereas others perform better at recursive listing. That said, the results are interesting nonetheless. Try navigating to the bonus folder and running the following commands:

```
$ python testing_flat_dir.py; python testing_nested_dir.py
Done!

RESULTS FLAT DIRECTORY:

os listdir     : 0.265 seconds
os scandir     : 0.338 seconds
os walk        : 0.430 seconds
iterdir        : 0.557 seconds
glob *         : 1.365 seconds
rglob          : 3.473 seconds
glob **/*      : 3.595 seconds

Done!

RESULTS NESTED DIRECTORY:

os scandir_gen : 1.116 seconds
os scandir     : 1.118 seconds
os walk        : 2.278 seconds
rglob          : 3.027 seconds
glob           : 3.494 seconds
os listdir     : 3.742 seconds
os listdir_gen : 3.775 seconds
iterdir        : 4.823 seconds
iterdir_gen    : 4.865 seconds
```

While the exact times will depend on your system, the relative speeds should be similar.

If you're running Python 3.12, you can uncomment some lines in `testing_flat_dir.py` and `testing_nested_dir.py` that'll enable testing for the new `walk()` method in the `pathlib` module.
