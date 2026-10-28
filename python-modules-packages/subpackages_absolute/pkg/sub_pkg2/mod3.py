def baz():
    print("[mod3] baz()")


class Baz:
    pass


from pkg.sub_pkg1.mod1 import foo  # noqa: E402

foo()
