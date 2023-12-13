# Python's Array: Working With Numeric Data Efficiently

Sample code for the [Python's Array: Working With Numeric Data Efficiently](https://realpython.com/python-array/) tutorial on Real Python.

## audio

Read 24-bit PCM-encoded audio samples from a WAV file:

```shell
$ cd audio/
$ python read_audio.py 
len(raw_bytes) = 793800
len(samples) = 264600
wave_file.getnframes() = 132300
samples.itemsize = 4
samples.itemsize * len(samples) = 1058400
```

## cruncher

Pass a Python array to a compiled C library:

```shell
$ cd cruncher/
$ gcc -shared -fPIC -O3 -o cruncher.so cruncher.c
$ python cruncher.py 
array('i', [-20, 14, -7, 6, -2, 3, 0, 2, 1, 2])
```

## save_load

Persist an array in a file and load it back into Python:

```shell
$ cd save_load/
$ python save_load.py
Saved array as: 'binary.data'
array('H', [12, 42, 7, 15, 42, 38, 21])
```
