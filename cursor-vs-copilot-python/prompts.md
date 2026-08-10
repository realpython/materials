# Prompts Used in Cursor vs GitHub Copilot

This file contains the prompts used in the **Cursor vs GitHub Copilot: Which AI Editor Is Better for Python?** comparison. The same prompts are used in both editors to compare how each editor handles the same development task.

## Project Setup

Use this prompt in **Agent** mode to set up the Markdown note manager project. It asks the editor to create the Python environment, install the required dependencies, add the test directory, and follow standard Python packaging conventions.

```text
Set up a Python project in this directory, following standard Python
packaging conventions:
- Create a virtual environment
- Install pyyaml==6.0.2 and pytest==9.0.3
- Add a tests/ directory
- Use the directory name as the package name
- Only include the dependencies listed above
```

## Implementing the Application

Use this prompt in **Agent** mode after setting up the project. It defines the requirements for the command-line Markdown note manager, including Markdown storage, YAML frontmatter, the note data model, SQLite persistence, and the command-line interface. :contentReference[oaicite:1]{index=1}

```text
Build a command-line Markdown note manager for this project.

Requirements:

- Store notes as Markdown files with YAML frontmatter containing a
  title and tags.
- Represent each note as a dataclass with title, body, tags, and
  created_at fields.
- Create a SQLite-backed NoteStore that can add notes, search notes,
  list notes by tag, and retrieve notes by title.
- Build an argparse command-line interface that exposes those
  operations.
```

## Testing and Debugging

Use this prompt in **Agent** mode after deliberately removing the `self._conn.commit()` call from `NoteStore.add_note()`. It asks the editor to run the existing tests, investigate any failures, fix the underlying problem, and verify the fix by running the complete test suite again. :contentReference[oaicite:2]{index=2}

```text
Run the existing pytest test suite.

If any tests fail, investigate the root cause, fix the underlying issue,
and rerun the tests until the entire suite passes.
```

## Planning the Archiving Feature

Use this prompt in **Plan** mode to compare how Cursor and GitHub Copilot plan a multi-file change before modifying the project. The feature adds support for archiving notes while keeping archived notes out of normal searches and listings unless explicitly requested. :contentReference[oaicite:3]{index=3}

```text
Create a plan to add support for archiving notes.

- Archived notes shouldn't appear in normal searches or listings.
- Add an `--include-archived` option to the search and list commands
  so archived notes can be included when needed.
- Integrate the feature cleanly with the existing application without
  introducing duplicate logic.
```

## Reviewing the Database Layer

Use this prompt in **Ask** mode after deliberately replacing the parameterized search query with an interpolated SQL query. It asks the editor to inspect the database layer for correctness, SQL safety, and code quality without changing the implementation. :contentReference[oaicite:4]{index=4}

```text
Review the database layer for correctness, SQL safety,
and general code quality.
Identify any issues and suggest improvements without modifying the code.
```

## Reviewing Pending Changes in Cursor

Use the `/review` command in Cursor after introducing the SQL injection vulnerability. Unlike the broader review in Ask mode, `/review` focuses on the changes in the current diff and identifies issues introduced by those changes. :contentReference[oaicite:5]{index=5}

```text
/review
```
