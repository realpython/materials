# Profiling in Python: How to Find Performance Bottlenecks

This folder holds sample code that supplements the Real Python tutorial [Profiling in Python: How to Find Performance Bottlenecks](https://realpython.com/python-profiling/).

## Profiler 1: `time`

```shell
$ python profile_time.py 
sleeper()
 Real time: 1.75 seconds
 CPU time: 0.00 seconds

spinlock()
 Real time: 1.80 seconds
 CPU time: 1.80 seconds
```

## Profiler 2: `timeit`

```shell
$ python profile_timeit.py 
Average time is 0.15 seconds
```

## Profiler 3: `cProfile`

```shell
$ python profile_cprofile.py 
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

## Profiler 4: `pyinstrument`

Make sure to install the third-party library [`pyinstrument`](https://pypi.org/project/pyinstrument/) from the supplied `requirements.txt` file into a virtual environment first:

```shell
$ python3 -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Then, you can run the sample script while you're still in the same virtual environment:

```shell
(venv) $ python profile_pyinstrument.py 
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

## Profiler 5: `perf`

Make sure to follow the setup instructions in the [Python 3.12 Preview: Support For the Linux perf Profiler](https://realpython.com/python312-perf-profiler/) tutorial.

Next, record samples into a local binary file named `perf.data`:

```shell
$ sudo perf record -g -F 999 $HOME/python-custom-build/bin/python3 -X perf profile_perf.py
```

Finally, display a report by issuing the following command while you're in the same folder:

```shell
$ sudo perf report
```

For an alternative view, try this instead:

```shell
$ sudo perf report --hierarchy --sort comm,dso,sample
```
