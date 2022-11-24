# Python `subprocess` Examples

Here are supporting materials for the Real Python tutorial, [The `subprocess` Module: Wrapping Programs With Python](https://realpython.com/python-subprocess/).

Be aware that some examples are designed for particular operating systems. The `basics_unix.py` file won't work on Windows, for instance.

Below are quick descriptions of what the different script do.

## [basics_unix.py](basics_unix.py)

**Only works on Linux or macOS**

Demonstrates basic usage of `subprocess.run()`

## [basics_win.py](basics_win.py)

**Only works on Windows**

Demonstrates basic usage of `subprocess.run()`

## [custom_exit.py](custom_exit.py)

Raises custom exit codes:

```shell
$ python custom_exit.py 3
```

This will exit with error code `3`. By default, will exit with code `0`

## [exiter_run.py](exiter_run.py)

Calls [custom_exit.py](custom_exit.py) with `subprocess.run()` demonstrating the `check` argument to `.run()`.

## [error_handling.py](error_handling.py)

Demonstrates error handling with `subprocess.run()`, catching common errors that `subprocess.run()` can encounter. Try changing the commands in `subprocess.run()` to raise different errors.

## [timer.py](timer.py)

Accepts an integer argument and will sleep for the given time. For example:

```
$ python timer.py 5
Starting timer of 5 seconds
.....Done!
```

## [popen_pipe.py](popen_pipe.py)

**Only works on Linux or macOS**

Demonstrates using `subprocess.Popen()` to pipe one command into the other.

## [popen_timer.py](popen_timer.py)

Demonstrates `subprocess.Popen()` calling [timer.py](timer.py)

## [random_num_gen.py](random_num_gen.py)

Generates and prints a random number.

## [random_num_gen_check_output.py](random_num_gen_check_output.py)

Uses `subprocess.run()` to call [random_num_gen.py](random_num_gen.py) to generate a random number, read the output, and then print it.

## [reaction_game.py](reaction_game.py)

Tests your reaction times.

Note that this game can be cheated by pressing enter before the game prompts you to press enter.

## [reaction_game_v2.py](reaction_game_v2.py)

Tests your reaction times, but guards against cheating by pressing enter before the game prompts you to by making you input a random letter instead.

## [reaction_game_v2_hack.py](reaction_game_v2_hack.py)

Uses `subprocess.Popen()` to cheat the second version of the reaction game.

## [create_project.py](create_project.py)

Creates a Python project, complete with a virtual environment and initialized Git repository.
