from fixtures import FakeFile, Files
from realpython import assert_equals_if, task, tutorial


@task(
    number=7,
    name="Read Data From Multiple Files",
    url="https://realpython.com/lessons/wordcount-read-data-from-multiple-files-task/",
)
@tutorial("python-for-loop", 'Python for Loops: The Pythonic Way')
@tutorial("python-list", "Python's list Data Type: A Deep Dive With Examples")
@tutorial(
    "list-comprehension-python", "When to Use a List Comprehension in Python"
)
class Test:
    def test_displays_counts_and_filenames_on_separate_lines(
        self, wc, medium_files
    ):
        assert wc(*medium_files.paths).startswith(medium_files.file_lines)

    def test_includes_a_summary_with_total_counts(self, wc, medium_files):
        assert wc(*medium_files.paths).endswith(medium_files.total_line)

    def test_can_repeat_the_same_file_multiple_times(self, wc, file1):
        files = Files([file1, file1, file1])
        assert_equals_if(files.expected, wc(*files.paths))

    def test_can_mix_files_with_standard_input(self, wc, file2):
        dash = FakeFile(b"caffe latte", (0, 2, 11, 11))
        files = Files([file2, dash])
        assert_equals_if(files.expected, wc(*files.paths, stdin=dash.content))

    def test_reports_a_directory_and_a_missing_file(
        self, wc, fake_dir, random_name
    ):
        assert_equals_if(
            b"".join(
                [
                    f"0 0 0 {fake_dir}/ (is a directory)\n".encode(),
                    f"0 0 0 {random_name} (no such file or directory)\n".encode(),
                    b"0 0 0 total\n",
                ]
            ),
            wc(fake_dir, random_name),
        )

    def test_reports_a_mix_of_all(self, wc, fake_dir, random_name, small_file):
        expected = b"".join(
            [
                f"0 0 0 {fake_dir}/ (is a directory)\n".encode(),
                small_file.format_line(),
                f"0 0 0 {random_name} (no such file or directory)\n".encode(),
                b"0 1 3\n",
                b"1 2 9 total\n",
            ]
        )
        assert_equals_if(
            expected,
            wc(fake_dir, str(small_file.path), random_name, "-", stdin=b"hot"),
        )
