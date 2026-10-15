# Test Snippets

Code changes used for the debugging, code completion, and code review tests in **Cursor vs GitHub Copilot: Which AI Editor Is Better for Python?**

## Debugging

Remove the `self._conn.commit()` call immediately after the SQLite insert operation in `NoteStore.add_note()`:

```python
self._conn.commit()
```

## AI Code Completion

### Add `updated_at`

Add an `updated_at` field to the `Note` dataclass after `created_at`:

```python
@dataclass
class Note:
    title: str
    body: str
    tags: list[str]
    created_at: datetime
    updated_at
```

### Rename the Search Method

Rename the `search_notes()` method:

```python
def search_notes(self, query: str) -> list[Note]:
```

to:

```python
def search(self, query: str) -> list[Note]:
```

## Code Review

Replace the parameterized `search_notes()` implementation with the corresponding vulnerable version.

### Cursor

Original:

```python
def search_notes(self, query: str) -> list[Note]:
    """
    Return notes whose title or body contains `query` (case-insensitive).
    """
    pattern = f"%{query}%"
    rows = self._conn.execute(
        """
        SELECT * FROM notes
        WHERE title LIKE ? COLLATE NOCASE
           OR body LIKE ? COLLATE NOCASE
        ORDER BY created_at DESC
        """,
        (pattern, pattern),
    ).fetchall()
    return [self._row_to_note(row) for row in rows]
```

Replace with:

```python
def search_notes(self, query: str) -> list[Note]:
    """
    Return notes whose title or body contains `query` (case-insensitive).
    """
    rows = self._conn.execute(
        f"""
        SELECT * FROM notes
        WHERE title LIKE '%{query}%' COLLATE NOCASE
           OR body LIKE '%{query}%' COLLATE NOCASE
        ORDER BY created_at DESC
        """
    ).fetchall()
    return [self._row_to_note(row) for row in rows]
```

### GitHub Copilot

Original:

```python
def search_notes(self, query: str) -> list[Note]:
    """Return notes whose title or body contains the given query text."""
    rows = self._conn.execute(
        """
        SELECT * FROM notes
        WHERE title LIKE ? OR body LIKE ?
        ORDER BY created_at
        """,
        (f"%{query}%", f"%{query}%"),
    ).fetchall()
    return [self._row_to_note(row) for row in rows]
```

Replace with:

```python
def search_notes(self, query: str) -> list[Note]:
    """Return notes whose title or body contains the given query text."""
    rows = self._conn.execute(
        f"""
        SELECT * FROM notes
        WHERE title LIKE '%{query}%'
           OR body LIKE '%{query}%'
        ORDER BY created_at
        """
    ).fetchall()
    return [self._row_to_note(row) for row in rows]
```
