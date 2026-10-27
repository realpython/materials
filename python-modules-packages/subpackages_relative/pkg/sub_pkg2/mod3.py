def baz():
    print("[mod3] baz()")


class Baz:
    pass


from .. import sub_pkg1  # noqa: E402

print(sub_pkg1)

from ..sub_pkg1.mod1 import foo  # noqa: E402

foo()
