from wordstats import top_words


def test_ignores_case_and_punctuation():
    assert top_words("The the THE, cat. Cat!", 2) == [("the", 3), ("cat", 2)]
