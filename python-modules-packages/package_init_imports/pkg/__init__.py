print(f"Invoking __init__.py for {__name__}")
import pkg.mod1, pkg.mod2  # noqa: E401, E402, F401
