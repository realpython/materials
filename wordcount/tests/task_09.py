from itertools import permutations

from realpython import assert_equals, task, tutorial


@task(
    number=9,
    name="Select Counts With Command-Line Options",
    url="https://realpython.com/lessons/wordcount-select-counts-with-command-line-options-task/",
)
@tutorial("python-bitwise-operators", "Bitwise Operators in Python")
@tutorial(
    "command-line-interfaces-python-argparse",
    "Build Command-Line Interfaces With Python's `argparse`",
)
@tutorial("python-enum", "Build Enumerations of Constants With Python's Enum")
@tutorial("lru-cache-python", "Caching in Python Using the LRU Cache Strategy")
@tutorial(
    "python-built-in-functions",
    "Managing Attributes: `getattr()`, `setattr()`, and `delattr()`",
    section="managing-attributes-getattr-setattr-and-delattr",
)
@tutorial(
    "python-or-operator",
    "Short-Circuit Evaluation",
    section="short-circuit-evaluation",
)
class Test:
    def test_counts_lines_words_bytes_by_default(self, wc, runner):
        """Counts lines, words, and bytes by default"""
        assert_equals(
            expected=b" 3  4 23\n",
            actual=wc(stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3),
                    b"  0   2  10\n",
                    runner.file2.format_line(max_digits=3),
                    f"  0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0   0\n",
                    runner.file3.format_line(max_digits=3),
                    f"  0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8  75 490 total\n",
                ]
            ),
            actual=runner(),
        )

    def test_counts_lines_words_bytes_explicitly(self, wc, runner):
        """Counts lines, words, and bytes explicitly"""
        flags = ["--lines", "--words", "--bytes"]
        assert_equals(
            expected=b" 3  4 23\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=13),
                    b"  0   2  10\n",
                    runner.file2.format_line(max_digits=3, selected=13),
                    f"  0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0   0\n",
                    runner.file3.format_line(max_digits=3, selected=13),
                    f"  0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8  75 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_only_counts_lines(self, wc, runner):
        flags = ["--lines"]
        assert_equals(
            expected=b"3\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(selected=8),
                    b"0\n",
                    runner.file2.format_line(selected=8),
                    f"0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"0\n",
                    runner.file3.format_line(selected=8),
                    f"0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"8 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_only_counts_words(self, wc, runner):
        flags = ["--words"]
        assert_equals(
            expected=b"4\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=2, selected=4),
                    b" 2\n",
                    runner.file2.format_line(max_digits=2, selected=4),
                    f" 0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b" 0\n",
                    runner.file3.format_line(max_digits=2, selected=4),
                    f" 0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"75 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_only_counts_bytes(self, wc, runner):
        flags = ["--bytes"]
        assert_equals(
            expected=b"23\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=1),
                    b" 10\n",
                    runner.file2.format_line(max_digits=3, selected=1),
                    f"  0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0\n",
                    runner.file3.format_line(max_digits=3, selected=1),
                    f"  0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_lines_and_words(self, wc, runner):
        flags = ["--lines", "--words"]
        assert_equals(
            expected=b"3 4\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=2, selected=12),
                    b" 0  2\n",
                    runner.file2.format_line(max_digits=2, selected=12),
                    f" 0  0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b" 0  0\n",
                    runner.file3.format_line(max_digits=2, selected=12),
                    f" 0  0 {runner.random_name} (no such file or directory)\n".encode(),
                    b" 8 75 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_lines_and_bytes(self, wc, runner):
        flags = ["--lines", "--bytes"]
        assert_equals(
            expected=b" 3 23\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=9),
                    b"  0  10\n",
                    runner.file2.format_line(max_digits=3, selected=9),
                    f"  0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0\n",
                    runner.file3.format_line(max_digits=3, selected=9),
                    f"  0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_words_and_bytes(self, wc, runner):
        flags = ["--words", "--bytes"]
        assert_equals(
            expected=b" 4 23\n",
            actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=5),
                    b"  2  10\n",
                    runner.file2.format_line(max_digits=3, selected=5),
                    f"  0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0\n",
                    runner.file3.format_line(max_digits=3, selected=5),
                    f"  0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b" 75 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_always_displays_counts_in_the_same_order(self, wc, runner):
        expected = b"".join(
            [
                runner.file1.format_line(max_digits=3),
                b"  0   2  10\n",
                runner.file2.format_line(max_digits=3),
                f"  0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                b"  0   0   0\n",
                runner.file3.format_line(max_digits=3),
                f"  0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                b"  8  75 490 total\n",
            ]
        )
        for flags in permutations(["--lines", "--words", "--bytes"]):
            assert_equals(
                expected=b" 3  4 23\n",
                actual=wc(*flags, stdin=b"caffe\nlatte\nflat white\n"),
            )
            assert_equals(expected=expected, actual=runner(*flags))
