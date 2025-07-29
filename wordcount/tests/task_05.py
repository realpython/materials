from realpython import assert_equals, task, tutorial


@task(
    number=5,
    name="Read Data From a File",
    url="https://realpython.com/lessons/wordcount-read-data-from-file-task/",
)
@tutorial("python-conditional-statements", "Conditional Statements in Python")
@tutorial(
    "python-pathlib", "Python's `pathlib` Module: Taming the File System"
)
@tutorial(
    "python-command-line-arguments",
    "The `sys.argv` Array",
    section="the-sysargv-array",
)
class Test:
    def test_displays_counts_and_a_filename_on_the_same_line(
        self, wc, small_files
    ):
        for file in small_files:
            assert_equals(file.format_line(), wc(str(file.path)))

    def test_treats_the_dash_character_as_standard_input(self, wc):
        """Treats the dash character (-) as standard input"""
        assert b"1 1 6\n" == wc("-", stdin=b"latte\n")
