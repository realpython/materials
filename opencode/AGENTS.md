# Agent Instructions: Dice Project

This document provides essential information for AI agents working on the Dice Project. Follow these guidelines to maintain consistency and ensure high-quality contributions.

## 1. Project Overview

The Dice Project is a lightweight Python CLI tool that simulates rolling one to six dice and displays the results using ASCII art.

- **Primary Language:** Python 3.x
- **Main Entry Point:** `dice.py`
- **Architecture:** Procedural script with functional decomposition.

## 2. Build, Run, and Test Commands

### Running the Application
To run the interactive CLI:
```bash
python dice.py
```

### Testing
There is currently no formal test suite. When adding tests:
- **Framework:** Use `pytest` (standard for this project).
- **Running all tests:** `pytest`
- **Running a single test file:** `pytest path/to/test_file.py`
- **Running a specific test:** `pytest path/to/test_file.py::test_function_name`

### Linting and Formatting
Maintain PEP 8 compliance. Recommended tools:
- **Linting:** `flake8 dice.py` or `ruff check dice.py`
- **Formatting:** `black dice.py`

## 3. Code Style Guidelines

### General Principles
- **Simplicity:** Keep the logic straightforward. Avoid over-engineering for a single-file utility.
- **Readability:** Prioritize clear, descriptive names over brevity.

### Naming Conventions
- **Functions:** Use `snake_case` (e.g., `generate_dice_faces_diagram`).
- **Variables:** Use `snake_case` (e.g., `roll_results`).
- **Constants:** Use `SCREAMING_SNAKE_CASE` (e.g., `DICE_ART`, `DIE_HEIGHT`).
- **Internal Helpers:** Prefix with a single underscore (e.g., `_get_dice_faces`).

### Imports
- Place standard library imports at the top of the file.
- Keep them alphabetized within their group.
- Example:
  ```python
  import random
  import sys
  ```

### Documentation
- Use triple-quoted docstrings for all functions.
- The first line should be a concise summary.
- Follow with a more detailed explanation if the function's logic or parameters aren't trivial.
- Example:
  ```python
  def roll_dice(num_dice):
      """Return a list of random integers between 1 and 6."""
      # implementation
  ```

### Formatting
- **Indentation:** 4 spaces.
- **Line Length:** Max 79-88 characters (standard PEP 8 / Black).
- **Vertical Spacing:** Two blank lines between top-level functions.

### Error Handling
- Use `parse_input` to validate user input.
- For fatal CLI errors, print a user-friendly message and use `raise SystemExit(1)`.
- Avoid broad `except Exception:` blocks; catch specific exceptions.

## 4. Project Conventions & Architecture

### ASCII Art Management
- All dice representations are stored in the `DICE_ART` dictionary.
- Each entry is a tuple of strings representing the rows of the die.
- Maintain the alignment and character usage (┌, ┐, └, ┘, │, ●) when modifying art.

### Main Execution Block
- Currently, the script executes its main logic at the bottom of the file.
- **Refactoring Target:** When modifying `dice.py`, consider wrapping the execution logic in an `if __name__ == "__main__":` block to allow for better testability and modularity.

### Input Validation
- All user inputs must be stripped and validated against expected values before processing.
- The `parse_input` function is the gatekeeper for valid dice counts.

## 5. External Rules

- **Cursor Rules:** No specific `.cursorrules` or `.cursor/rules/` detected.
- **Copilot Instructions:** No `.github/copilot-instructions.md` detected.
- **Standard Guidelines:** Default to standard Python best practices (PEP 8, PEP 257).

## 6. Task-Specific Instructions

### When Adding Features
1.  **Check for side effects:** Ensure changes to `DICE_ART` don't break `generate_dice_faces_diagram`.
2.  **Maintain ASCII alignment:** Use `DIE_HEIGHT` and `DIE_WIDTH` constants to ensure the diagram remains rectangular.
3.  **Self-Verification:** After making changes, run `python dice.py` and test with various inputs (1, 6, and invalid strings) to ensure the CLI still behaves as expected.

### When Refactoring
- Ensure that helper functions remain "private" (prefixed with `_`) if they are not intended for external use.
- Maintain the docstring style and clarity.

## Python Guidelines

- Follow PEP 8 style conventions
- Add type hints to all new and modified functions
- Prefer specific exception types over bare `except` clauses
- Use context managers for file I/O and database connections
- Write descriptive error messages that include the offending value

---
*Note: This file is intended for AI agents. If you are a human, feel free to update these guidelines as the project evolves.*
