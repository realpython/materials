from realpython import assert_equals, task, tutorial


@task(
    number=8,
    name="Ensure Consistent Number Formatting",
    url="https://realpython.com/lessons/wordcount-consistent-formatting-task/",
)
@tutorial("python-data-classes", "Data Classes in Python (Guide)")
@tutorial(
    "python-multiple-constructors",
    "Providing Multiple Constructors in Your Python Classes",
)
@tutorial(
    "python-classes",
    "Python Classes: The Power of Object-Oriented Programming",
)
@tutorial(
    "python-magic-methods",
    "Python's Magic Methods: Leverage Their Power in Your Classes",
)
@tutorial(
    "python-property",
    "Python's property(): Add Managed Attributes to Your Classes",
)
@tutorial(
    "python-repr-vs-str",
    "When Should You Use .__repr__() vs .__str__() in Python?",
)
@tutorial("python-namedtuple", "Write Pythonic and Clean Code With namedtuple")
class Test:
    def test_uses_consistent_formatting_across_lines(
        self, wc, small_file, unicode_file, big_file, fake_dir, random_name
    ):
        expected = b"".join(
            [
                small_file.format_line(max_digits=3),
                b"  0   2  10\n",
                unicode_file.format_line(max_digits=3),
                f"  0   0   0 {fake_dir}/ (is a directory)\n".encode(),
                b"  0   0   0\n",
                big_file.format_line(max_digits=3),
                f"  0   0   0 {random_name} (no such file or directory)\n".encode(),
                b"  8  75 490 total\n",
            ]
        )
        actual = wc(
            str(small_file.path),
            "-",
            str(unicode_file.path),
            fake_dir,
            "-",
            str(big_file.path),
            random_name,
            stdin=b"flat white",
        )
        assert_equals(expected, actual)
