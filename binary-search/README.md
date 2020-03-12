# How to Do a Binary Search in Python

Code snippets supplementing the [How to Do a Binary Search in Python](https://realpython.com/binary-search-python/) article.

## Usage

### Download Sample Dataset

To download a sample dataset for benchmarking, run the following script:

```shell
$ python download_imdb.py
Fetching data from IMDb...
Created "names.txt" and "sorted_names.txt"
```

### Benchmark

**Note:** The hash-based search algorithm requires a separate data structure, so it's not included here. Feel free to treat it as an exercise.

Find the index of Arnold Schwarzenegger in unsorted names using random search:

```shell
$ python benchmark.py -a random -f names.txt 'Arnold Schwarzenegger'
Loading names...ok
[1/10] Found at index=215 (21.68 s)
[2/10] Found at index=215 (148.10 ms)
[3/10] Found at index=215 (63.49 s)
[4/10] Found at index=215 (15.93 s)
[5/10] Found at index=215 (23.38 s)
[6/10] Found at index=215 (60.98 s)
[7/10] Found at index=215 (10.14 s)
[8/10] Found at index=215 (15.81 s)
[9/10] Found at index=215 (5.10 s)
[10/10] Found at index=215 (13.36 s)
best=148.10 ms, worst=63.49 s, avg=23.00 s, median=15.87 s
```

Find the index of Arnold Schwarzenegger in unsorted names using linear search:

```shell
$ python benchmark.py -a linear -f names.txt 'Arnold Schwarzenegger'
Loading names...ok
[1/10] Found at index=215 (30.95 µs)
[2/10] Found at index=215 (26.86 µs)
[3/10] Found at index=215 (26.26 µs)
[4/10] Found at index=215 (26.55 µs)
[5/10] Found at index=215 (26.24 µs)
[6/10] Found at index=215 (25.88 µs)
[7/10] Found at index=215 (25.77 µs)
[8/10] Found at index=215 (25.89 µs)
[9/10] Found at index=215 (25.91 µs)
[10/10] Found at index=215 (25.99 µs)
best=25.77 µs, worst=30.95 µs, avg=26.63 µs, median=26.11 µs
```

Find the index of Arnold Schwarzenegger in *sorted* names using binary search:

```shell
$ python benchmark.py -a binary -f sorted_names.txt 'Arnold Schwarzenegger'
Loading names...ok
[1/10] Found at index=782431 (18.82 µs)
[2/10] Found at index=782431 (9.19 µs)
[3/10] Found at index=782431 (11.08 µs)
[4/10] Found at index=782431 (9.70 µs)
[5/10] Found at index=782431 (10.14 µs)
[6/10] Found at index=782431 (9.35 µs)
[7/10] Found at index=782431 (9.42 µs)
[8/10] Found at index=782431 (8.79 µs)
[9/10] Found at index=782431 (8.66 µs)
[10/10] Found at index=782431 (8.79 µs)
best=8.66 µs, worst=18.82 µs, avg=10.39 µs, median=9.38 µs
```
