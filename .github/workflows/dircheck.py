"""
Linter to ensure standard folder structure
"""
import pathlib
import re
import sys

IGNORELIST = {
    "venv",
    "asyncio-walkthrough",
    "build-a-gui-with-wxpython",
    "consuming-apis-python",
    "flask-connexion-rest-part-3",
    "flask-connexion-rest-part-4",
    "generators",
    "intro-to-threading",
    "introduction-combining-data-pandas-merge-join-and-concat",
    "linked-lists-python",
    "nearbyshops",
    "oop-in-java-vs-python",
    "opencv-color-spaces",
    "openpyxl-excel-spreadsheets-python",
    "pygame-a-primer",
    "pyqt-calculator-tutorial",
    "python-dash",
    "python-eval-mathrepl",
    "rp-portfolio",
    "storing-images",
    "understanding-asynchronous-programming",
}
FOLDER_NAME_RE = re.compile(r"^[-a-z0-9]{5,}\Z")

has_errors = False

for f in sorted(pathlib.Path(".").glob("*")):
    if not f.is_dir():
        continue
    if str(f).startswith("."):
        continue
    if str(f) in IGNORELIST:
        continue

    if not FOLDER_NAME_RE.search(str(f)):
        print(
            f"{f}: ensure folder name only uses "
            f"lowercase letters, numbers, and hyphens"
        )
        has_error = True

    files = sorted(_.name for _ in f.glob("*"))
    if "README.md" not in files:
        print(f"{f}: no README.md found")
        has_errors = True

if has_errors:
    print(
        """-----------------------
Please ensure new sample projects are added using the correct
folder structure:

  * New files should go into a top-level subfolder, named after the
    article slug (lowercase, dashes). For example: my-awesome-article/

  * Top-level sample project folders should contain a README.md file.
    For example: my-awesome-article/README.md

This helps us keep the repo clean and easy to browse on GitHub.

Thanks!
"""
    )
    sys.exit(1)
