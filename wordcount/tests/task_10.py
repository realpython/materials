from itertools import permutations

import pytest
from realpython import TEST_TIMEOUT_SECONDS, assert_equals, task


@task(
    number=10,
    name="Add Support for Counting the Characters",
    url="https://realpython.com/lessons/wordcount-add-support-for-counting-the-characters-task/",
)
class Test:
    def test_only_counts_characters(self, wc, runner):
        flags = ["--chars"]
        assert_equals(
            expected=b"18\n",
            actual=wc(*flags, stdin="zażółć\ngęślą\njaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=2),
                    b" 10\n",
                    runner.file2.format_line(max_digits=3, selected=2),
                    f"  0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0\n",
                    runner.file3.format_line(max_digits=3, selected=2),
                    f"  0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"481 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_characters_and_bytes(self, wc, runner):
        flags = ["--chars", "--bytes"]
        assert_equals(
            expected=b"18 27\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=3),
                    b" 10  10\n",
                    runner.file2.format_line(max_digits=3, selected=3),
                    f"  0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0\n",
                    runner.file3.format_line(max_digits=3, selected=3),
                    f"  0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"481 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_words_and_characters(self, wc, runner):
        flags = ["--words", "--chars"]
        assert_equals(
            expected=b" 3 18\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=6),
                    b"  2  10\n",
                    runner.file2.format_line(max_digits=3, selected=6),
                    f"  0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0\n",
                    runner.file3.format_line(max_digits=3, selected=6),
                    f"  0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b" 75 481 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_words_characters_bytes(self, wc, runner):
        """Counts words, characters, and bytes"""
        flags = ["--words", "--chars", "--bytes"]
        assert_equals(
            expected=b" 3 18 27\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=7),
                    b"  2  10  10\n",
                    runner.file2.format_line(max_digits=3, selected=7),
                    f"  0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0   0\n",
                    runner.file3.format_line(max_digits=3, selected=7),
                    f"  0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b" 75 481 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_lines_and_characters(self, wc, runner):
        flags = ["--lines", "--chars"]
        assert_equals(
            expected=b" 2 18\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=10),
                    b"  0  10\n",
                    runner.file2.format_line(max_digits=3, selected=10),
                    f"  0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0\n",
                    runner.file3.format_line(max_digits=3, selected=10),
                    f"  0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8 481 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_lines_characters_bytes(self, wc, runner):
        """Counts lines, characters, and bytes"""
        flags = ["--lines", "--chars", "--bytes"]
        assert_equals(
            expected=b" 2 18 27\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=11),
                    b"  0  10  10\n",
                    runner.file2.format_line(max_digits=3, selected=11),
                    f"  0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0   0\n",
                    runner.file3.format_line(max_digits=3, selected=11),
                    f"  0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8 481 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_lines_words_characters(self, wc, runner):
        """Counts lines, words, and characters"""
        flags = ["--lines", "--words", "--chars"]
        assert_equals(
            expected=b" 2  3 18\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=14),
                    b"  0   2  10\n",
                    runner.file2.format_line(max_digits=3, selected=14),
                    f"  0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0   0\n",
                    runner.file3.format_line(max_digits=3, selected=14),
                    f"  0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8  75 481 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    def test_counts_lines_words_characters_bytes(self, wc, runner):
        """Counts lines, words, characters, and bytes"""
        flags = ["--lines", "--words", "--chars", "--bytes"]
        assert_equals(
            expected=b" 2  3 18 27\n",
            actual=wc(*flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")),
        )
        assert_equals(
            expected=b"".join(
                [
                    runner.file1.format_line(max_digits=3, selected=15),
                    b"  0   2  10  10\n",
                    runner.file2.format_line(max_digits=3, selected=15),
                    f"  0   0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                    b"  0   0   0   0\n",
                    runner.file3.format_line(max_digits=3, selected=15),
                    f"  0   0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                    b"  8  75 481 490 total\n",
                ]
            ),
            actual=runner(*flags),
        )

    @pytest.mark.timeout(TEST_TIMEOUT_SECONDS * 4)
    def test_always_displays_counts_in_the_same_order(self, wc, runner):
        expected = b"".join(
            [
                runner.file1.format_line(max_digits=3, selected=15),
                b"  0   2  10  10\n",
                runner.file2.format_line(max_digits=3, selected=15),
                f"  0   0   0   0 {runner.fake_dir}/ (is a directory)\n".encode(),
                b"  0   0   0   0\n",
                runner.file3.format_line(max_digits=3, selected=15),
                f"  0   0   0   0 {runner.random_name} (no such file or directory)\n".encode(),
                b"  8  75 481 490 total\n",
            ]
        )
        for flags in permutations(
            ["--lines", "--words", "--chars", "--bytes"]
        ):
            assert_equals(
                expected=b" 2  3 18 27\n",
                actual=wc(
                    *flags, stdin="zażółć\ngęślą jaźń\n".encode("utf-8")
                ),
            )
            assert_equals(expected=expected, actual=runner(*flags))
