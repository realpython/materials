# How to Define the Acceptance Criteria?

## File Naming

In your project's `tests/` directory, create one or more Python source files (`.py`) corresponding to each task in the coding challenge. These files must follow a certain naming convention: `task_?\d+.py`.

Here are a few examples:

```
task5.py
task05.py
task_05.py
```

This naming convention makes these files recognizable by the pytest-realpython plugin, which ignores standard pytest files prefixed or suffixed with the word "test." At the same time, users can run regular unit tests by disabling the plugin, e.g., with `pytest -p no:realpython`.

## Registering Acceptance Criteria for Each Task

Inside each task file, create a class decorated with the `@task()` decorator:

```python
from realpython import task

@task(
    number=1,
    name="Run the wordcount Command",
    url="https://realpython.com/lessons/run-the-wordcount-command-task/",
)
class Test:
    def test_one(self):
        ...
    
    def test_two(self):
        ... 

    def test_three(self):
        ...
```

This class can be named anything, e.g., `Test`, and you can reuse this name across different files if you want to.

Task numbering starts at one and there cannot be any duplicates or gaps between task numbers. The plugin will enforce that, or else you'll get an error.

Note that you can have at most one test class per task, so you won't be able to spread your test methods across multiple classes for the same task. This is to ensure a single source of truth. Otherwise, different classes could use inconsistent task names or URLs, which would be prone to copy-paste errors.

## Associating Resources With Tasks and Acceptance Criteria

If a particular test fails a few times, the report displays a list of clickable links that point to Real Python resources, including:

- Written Tutorials
- Video Courses
- Podcast Episodes
- Learning Paths

You can associate resources common to all test methods by placing the corresponding decorator on the test class, e.g.:

```python
from realpython import task, tutorial, course, podcast

@task(
    number=1,
    name="Run the wordcount Command",
    url="https://realpython.com/lessons/run-the-wordcount-command-task/",
)
@tutorial("python-comments-guide")
@course("writing-comments-python", "Writing Comments in Python")
class Test:
    ...
```

This will cascade down to the individual test methods, meaning that if one of them fails, then we'll include that resource on the list of hints. 

In contrast, decorating the individual test methods will let you associate resources unique to the acceptance criterion at hand:

```python
from realpython import task, tutorial, course, podcast

@task(
    number=1,
    name="Run the wordcount Command",
    url="https://realpython.com/lessons/run-the-wordcount-command-task/",
)
class Test:
    
    def test_one(self):
        ...
    
    @course("writing-comments-python", "Writing Comments in Python")
    def test_two(self):
        ...
    
    @tutorial("python-comments-guide")
    def test_three(self):
        ...
```

These decorators expect the **slug** to identify a resource in the CMS. If you don't provide a title, which is an optional parameter, then the slug will be automatically prettified and used as a link label.

## Making the Acceptance Criteria Look Pretty

By default, the plugin will try to prettify the acceptance criteria shown in the report based on the name of the corresponding test method, e.g.:

```python
def test_reports_zeros_on_an_empty_stream(self):
    ...
```

...becomes "_Reports zeros on an empty stream_."

If you'd like to use special characters or punctuation, which are not valid Python syntax, then you can define a docstring in the test method, which will override the method name:

```python
def test_count_default_stdin(self):
    """Counts lines, words, and bytes in stdin by default"""
```

## Parameterizing Test Methods

pytest allows you to run the same test method against different parameters (data-driven testing). The pytest-realpython plugin supports this, so you can do the following:

```python
import pytest

@pytest.mark.parametrize("flags", [
    [],
    ["-l"],
    ["-w"],
    ["-c"],
    ["-l", "-w", "-c"],
])
def test_always_displays_counts_in_the_same_order(self, flags):
    ...
```

The resulting report will append the values of the parameters to the name of the acceptance criteria. This will work regardless of whether you provde a docstring or not.  

## Overriding the Default Timeout of Individual Test Methods

By default, each test method will time out after a predefined number of seconds. If you'd like to override this default timeout, then use a decorator from the pytest-timeout plugin, like so:

```python
import pytest

@task(...)
class Test:
    @pytest.mark.timeout(3.5)
    def test_one(self):
        ...
```

## Running Tests in DEBUG Mode

The plugin disables the `terminalreporter` plugin, which is responsible for pytest's standard output. This is nice for running tests in "production" but hides tracebacks that might be useful during development. To include this core plugin, you can set the `DEBUG` environment variable:

```sh
$ DEBUG=1 pytest
```

Moreover, if something catastrophic happens while running tests, i.e., when the pytest-realpython plugin raises an exception, then we don't show the report. Instead, we print the stack trace.

Also, it can be useful to preview the pytest cache sometimes:

```sh
$ pytest --cache-show
```

## Writing Assertions

You can use pytest's standard assertions, i.e.:

```python
def test_one(self):
    assert "foo" == "bar"
```

Unfortunately, the `terminalreporter` plugin, which is disabled, tightly couples printing to stdout and collecting test results, rewriting the `assert` statements with custom bytecode instructions. This means that we no longer get the nice output of failed assertions that pytest provides.

As a workaround, you can append an optional message that will appear as a hint in the test report summary:

```python
def test_one(self):
    assert "expected" == function(), "Be careful about handling this and that"
```

However, it sill won't show the **expected vs. actual**. If you want to do that, then you must use a custom assertion function provided by the pytest-realpython plugin:

```python
from realpython import task, assert_equals

@task(...)
class Test:
    def test_one(self):
        assert_equals(
            "expected",
            function(),
            "Your function should return XYZ"
        )
```

Note that the order of these arguments matters! The _expected_ value always comes first! Therefore, it's a good idea to be explicit and use named arguments:

```python
from realpython import task, assert_equals

@task(...)
class Test:
    def test_one(self):
        assert_equals(
            expected="expected",
            actual=function(),
            message="Your function should return XYZ"
        )
```

If you just want to show the expected vs actual without any extra message, then you can omit the third argument:

```python
from realpython import task, assert_equals

@task(...)
class Test:
    def test_one(self):
        assert_equals("expected", function())
```

Note that the messages support the Markdown syntax, so you can include links and the desired font formatting.

## Using the CLI

Run all test methods up to the current task:

```sh
$ pytest
```

When all the acceptance criteria so far are passed, you advance to the next task, unlocking it.

Run only the failed tests:

```shell
$ pytest --last-failed
```

Run the test methods of a specific task:

```sh
$ pytest -k 5
$ pytest -k 10
$ pytest -k 01
```

Note that typing `-k 1` would run both task_01 and task_10 because it's an expression to be matched against pytest's node id.

Erase the progress to start from scratch (without deleting or reverting Python source files):

```sh
$ pytest --cache-clear
```
