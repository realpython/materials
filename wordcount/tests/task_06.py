from realpython import task, tutorial


@task(
    number=6,
    name="Ignore Directories and Missing Files",
    url="https://realpython.com/lessons/wordcount-ignore-invalid-paths-task/",
)
@tutorial("python-exceptions", "Python Exceptions: An Introduction")
@tutorial(
    "python-built-in-exceptions",
    "Python's Built-in Exceptions: A Walkthrough With Examples",
)
class Test:
    def test_reports_zeros_on_a_directory(self, wc, fake_dir):
        expected = f"0 0 0 {fake_dir}/ (is a directory)\n".encode()
        assert expected == wc(fake_dir)

    def test_reports_zeros_on_a_missing_file(self, wc, random_name):
        expected = (
            f"0 0 0 {random_name} (no such file or directory)\n".encode()
        )
        assert expected == wc(random_name)
