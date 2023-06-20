# Python 3.12 Preview: `perf` Profiler

This folder contains sample code for the [Python 3.12 Preview: Support For the Linux `perf` Profiler](https://realpython.com/python312-perf-profiler/) tutorial hosted on Real Python.

## 🛠️ Setup

### Python 3.12

Download, build, and install Python 3.12 from the source code with the frame pointer optimizations disabled:

```shell
$ git clone --branch v3.12.0b2 https://github.com/python/cpython.git
$ cd cpython/
$ export CFLAGS='-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer'
$ ./configure --prefix="$HOME/python-custom-build"
$ make -j $(nproc)
$ make install
```

### Virtual Environment

Create and activate a new virtual environment based on Python 3.12:

```shell
$ "$HOME/python-custom-build/bin/python3" -m venv venv/ --prompt 'py3.12-custom'
$ source venv/bin/activate
```

### Dependencies

Install dependencies from the `requirements.txt` file into your virtual environment:

```shell
(py3.12-custom) $ python -m pip install -r requirements.txt
```

## 🏃‍♂️ Run Existing Profilers

### Profiler 1: `time`

```shell
(py3.12-custom) $ python profile_time.py 
sleeper()
 Real time: 1.75 seconds
 CPU time: 0.00 seconds

spinlock()
 Real time: 1.80 seconds
 CPU time: 1.80 seconds
```

### Profiler 2: `timeit`

```shell
(py3.12-custom) $ python profile_timeit.py 
Average time is 0.15 seconds
```

### Profiler 3: `cProfile`

```shell
(py3.12-custom) $ python profile_cprofile.py 
fib(35) = 9227465
         29860712 function calls (10 primitive calls) in 9.487 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
29860703/1    9.487    0.000    9.487    9.487 profile_cprofile.py:5(fib)
        1    0.000    0.000    0.000    0.000 pstats.py:118(init)
        1    0.000    0.000    0.000    0.000 pstats.py:137(load_stats)
        1    0.000    0.000    0.000    0.000 pstats.py:108(__init__)
        1    0.000    0.000    0.000    0.000 cProfile.py:51(create_stats)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
```

### Profiler 4: `pyinstrument`

```shell
(py3.12-custom) $ python profile_pyinstrument.py 
n = 10         [2.8, 2.8, 2.8, 3.2, 2.4]
n = 100        [3.04, 3.28, 3.24, 2.92, 3.24]
n = 1,000      [3.176, 3.192, 3.188, 3.076, 3.132]
n = 10,000     [3.1376, 3.1328, 3.172, 3.1292, 3.1376]
n = 100,000    [3.14636, 3.13424, 3.15104, 3.14212, 3.14612]
n = 1,000,000  [3.141736, 3.141708, 3.14168, 3.141828, 3.140708]
n = 10,000,000 [3.14143, 3.1403824, 3.1411704, 3.1408808, 3.1420068]

  _     ._   __/__   _ _  _  _ _/_   Recorded: 11:49:03  Samples:  243
 /_//_/// /_\ / //_// / //_'/ //     Duration: 24.334    CPU time: 24.298
/   _/                      v4.5.0

Program: profile_pyinstrument.py

24.300 <module>  profile_pyinstrument.py:1
└─ 24.300 estimate_pi  profile_pyinstrument.py:6
   ├─ 23.200 <genexpr>  profile_pyinstrument.py:7
   │  ├─ 15.200 point  profile_pyinstrument.py:14
   │  │  ├─ 7.700 Random.uniform  random.py:520
   │  │  │     [4 frames hidden]  random, <built-in>
   │  │  │        6.200 [self]  None
   │  │  └─ 7.500 [self]  None
   │  ├─ 4.600 [self]  None
   │  └─ 3.400 hits  profile_pyinstrument.py:10
   │     ├─ 2.400 [self]  None
   │     └─ 1.000 abs  None
   │           [2 frames hidden]  <built-in>
   └─ 1.100 [self]  None
```

## ⏲️ Profile Python With `perf`

Record Samples:

```shell
$ cd benchmark/
$ sudo perf record -g -F max ../venv/bin/python -X perf benchmark.py
```

Display reports:

```shell
$ cd benchmark/
$ sudo perf report
$ sudo perf report --stdio -g
$ sudo perf report --hierarchy --verbose --call-graph fractal --sort sample,dso
```

## 🔥 Flame Graphs

Download Perl scripts and add them to your `$PATH` environment variable:

```shell
$ git clone git@github.com:brendangregg/FlameGraph.git
$ export PATH="$(pwd)/FlameGraph:$PATH"
```

Generate the flame graph and save it to a local file:

```shell
$ cd benchmark/
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
