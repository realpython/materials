from realpython import external, task, tutorial


@task(
    number=3,
    name="Handle Non-ASCII Unicode Characters",
    url="https://realpython.com/lessons/wordcount-handle-non-ascii-characters-task/",
)
@external(
    url="https://docs.python.org/3/howto/unicode.html#python-s-unicode-support",
    title="Python's Unicode Support",
)
@tutorial(
    "python-encodings-guide",
    "Unicode & Character Encodings in Python: A Painless Guide",
)
@tutorial(
    "read-write-files-python", "Reading and Writing Files in Python (Guide)"
)
class Test:
    def test_decodes_multibyte_character_without_trailing_newline(self, wc):
        """Decodes a multi-byte character without a trailing newline"""
        hint = "Note the difference between _e_ and _è_, for example."
        assert b"0 1 6\n" == wc(stdin=b"caff\xc3\xa8"), hint

    def test_decodes_multibyte_character_with_trailing_newline(self, wc):
        """Decodes a multi-byte character with a trailing newline"""
        assert b"1 1 7\n" == wc(stdin=b"caff\xc3\xa8\n")
