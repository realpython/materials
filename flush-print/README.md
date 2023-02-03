# How to Flush the Output of the Python Print Function

This directory contains code associated with the Real Python tutorial [How to Flush the Output of the Python Print Function](https://realpython.com/python-flush-print-output/).

## Installation

You don't need to install anything apart from a Python interpreter >=3.6 to run the example files.

## Countdown Script Variations

You can find all the code snippets that you've seen in the tutorial. For convenience, they're provided as separate files that all start with `countdown` and describe their differences with the rest of the filename. To see all the examples shown in the tutorial, you can run each of the files separately without needing to edit the code. Please visit the tutorial link for additional context.

## Terminal Based Visual Progress Indicators

Additionally, this directory also contains two scripts that show example implementations of terminal animations that you can build using `print()` and its parameters:

- [`spinner.py`](spinner.py)
- [`progress.py`](progress.py)

Both of them utilize explicit flushing, and you can learn more about how to build them in [Your Guide to the Python `print()` Function](https://realpython.com/python-print/).

## Buffer Size Approximations

Finally, if you're curious to dive somewhat deeper into the rabbit hole of buffering in Python, you can take a look at [`buffersize.py`](buffersize.py).

There doesn't seem to be a way to get the size of the default buffer for stdout on your operating system directly through a Python object. If you know or find a way, please [contact the author](#about-the-author). I'd be very curious to know :)

This script gives you a way to approximate the buffer size that Python uses when writing to stdout on your operating system and configuration. Note that this can be quite different across different setups.

The approach to calculate it is somewhat manual:

1. Run the script.
2. Note if the numbers that it prints pause in between before the script finishes execution.
  - If they pause, remember the last number that got printed before the pause.
  - If they don't pause, increase the value of `SLIGHTLY_TOO_LARGE_FOR_BUFFER` by `10_000` and start from the top.

Continue doing this until your script pauses when printing the numbers, and note the number that displays last during the pause. Once you have that number, manually subtract it from the value that `SLIGHTLY_TOO_LARGE_FOR_BUFFER` currently has to calculate your buffer size estimation. For example:

```python
SLIGHTLY_TOO_LARGE_FOR_BUFFER = 80_000

# Script paused at 10919

bufsize = 80_000 - 10919
print(bufsize) # 69081 <-- Your buffer size approximation
```

You can divide the number you get by `1000` to get an estimation of your buffer size for stdout in kilobytes. In the example above, on a macOS system with a M1 chip, the buffer size of stdout when interacting with it through Python's `print()` would therefore be approximately 69 kilobytes.

If you want to, you could even drill down further with some manual binary search to find the exact byte when the break first occurs.

The idea of this script is that each of these printed numbers take up exactly 6 bytes in the buffer. This is assuming that you're using an encoding in which numbers and spaces take up one byte. If so, then you can make sure each length is 6 characters with the format specifier in the f-string that you pass to `print()`.

At some point, the buffer gets filled up so much that it needs to flush during the execution of your script. After it's flushed, it'll begin to fill up again. Ideally before it fills up again, you run into the call to `time.sleep()` executing. Finally, when the script finishes execution after the sleep, Python flushes the rest of the buffer contents, which prints the remaining numbers to your terminal.

Finally, you need to subtract from the current value of `SLIGHTLY_TOO_LARGE_FOR_BUFFER` because we assume that the buffer flushes continuously when it gets full, which means that whatever is in the buffer when the script is done should represent a full buffer.

## About the Author

Martin Breuss - Email: martin@realpython.com

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
