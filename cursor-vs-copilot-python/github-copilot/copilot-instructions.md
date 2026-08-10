## GitHub Copilot Repository Instructions

This project includes Repository Instructions that define the coding conventions GitHub Copilot should follow when working with the Markdown note manager.

The instructions are stored in `.github/copilot-instructions.md` and provide repository-wide guidance for Copilot.

```markdown
# Repository Instructions

- Use type hints for all functions, return values, and dataclass fields.
- Parse YAML frontmatter with `yaml.safe_load()`. Do not manually parse YAML.
- Use `pathlib.Path` for all file and directory operations.
- Use parameterized SQL queries for every SQLite operation.
- Represent notes as dataclasses rather than dictionaries.
```
