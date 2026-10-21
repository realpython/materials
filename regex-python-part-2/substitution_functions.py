"""Substitution functions: re.sub() and re.subn()."""

import re


def f(match_obj):
    s = match_obj.group(0)  # The matching string

    # s.isdigit() returns True if all characters in s are digits
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()


if __name__ == "__main__":
    # Substitution by string
    s = "foo.123.bar.789.baz"
    print(re.sub(r"\d+", "#", s))
    # foo.#.bar.#.baz
    print(re.sub("[a-z]+", "(*)", s))
    # (*).123.(*).789.(*)

    # Numbered and named backreferences in the replacement string
    print(
        re.sub(
            r"(\w+),bar,baz,(\w+)",
            r"\2,bar,baz,\1",
            "foo,bar,baz,qux",
        )
    )
    # qux,bar,baz,foo
    print(
        re.sub(
            r"foo,(?P<w1>\w+),(?P<w2>\w+),qux",
            r"foo,\g<w2>,\g<w1>,qux",
            "foo,bar,baz,qux",
        )
    )
    # foo,baz,bar,qux
    print(
        re.sub(
            r"foo,(\w+),(\w+),qux",
            r"foo,\g<2>,\g<1>,qux",
            "foo,bar,baz,qux",
        )
    )
    # foo,baz,bar,qux

    # \10 is read as a reference to group 10, so use \g<1> instead
    try:
        re.sub(r"(\d+)", r"\10", "foo 123 bar")
    except re.error as e:  # re.PatternError in Python 3.13+
        print(f"{type(e).__name__}: {e}")
    # PatternError: invalid group reference 10 at position 1
    print(re.sub(r"(\d+)", r"\g<1>0", "foo 123 bar"))
    # foo 1230 bar
    print(re.sub(r"\d+", r"/\g<0>/", "foo 123 bar"))
    # foo /123/ bar

    # A zero-length match substitutes at every character position
    print(re.sub("x*", "-", "foo"))
    # -f-o-o-

    # Substitution by function
    print(re.sub(r"\w+", f, "foo.10.bar.20.baz.30"))
    # FOO.100.BAR.200.BAZ.300

    # Limiting the number of replacements
    print(re.sub(r"\w+", "xxx", "foo.bar.baz.qux"))
    # xxx.xxx.xxx.xxx
    print(re.sub(r"\w+", "xxx", "foo.bar.baz.qux", count=2))
    # xxx.xxx.baz.qux

    # re.subn() also returns the number of substitutions made
    print(re.subn(r"\w+", "xxx", "foo.bar.baz.qux"))
    # ('xxx.xxx.xxx.xxx', 4)
    print(re.subn(r"\w+", "xxx", "foo.bar.baz.qux", count=2))
    # ('xxx.xxx.baz.qux', 2)
    print(re.subn(r"\w+", f, "foo.10.bar.20.baz.30"))
    # ('FOO.100.BAR.200.BAZ.300', 6)
