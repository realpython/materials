"Number" if isinstance(3.14, (int, float)) else "Not a number"

"Number" if isinstance("3.14", (int, float)) else "Not a number"

"Number" if isinstance(3.14, ((int, float), (bool,))) else "Not a number"

"Number" if isinstance(3.14, (int, float, bool)) else "Not a number"

"Number" if isinstance(3.14, int | float) else "Not a number"

"Number" if isinstance("3.14", int | float) else "Not a number"
