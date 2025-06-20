import os
from subprocess import run

from realpython import assert_equals, course, task, tutorial


@task(
    number=1,
    name="Run the wordcount Command",
    url="https://realpython.com/lessons/wordcount-run-command-task/",
)
@tutorial("defining-your-own-python-function")
@tutorial("terminal-commands", "The Terminal: First Steps and Useful Commands")
@tutorial("python-pass", "The `pass` Statement: How to Do Nothing in Python")
@course("using-terminal-linux", "Using the Terminal on Linux")
@tutorial("python-comments-guide", "Writing Comments in Python (Guide)")
@course("writing-comments-python", "Writing Comments in Python")
class Test:
    def test_command_returns_successfully(self):
        process = run(["wordcount", os.devnull], capture_output=True)
        assert_equals(
            expected=0,
            actual=process.returncode,
            message=(
                "The process should return a zero [exit status]"
                "(https://en.wikipedia.org/wiki/Exit_status) code"
            ),
        )
