# Prompts

Copy-paste these into Cursor and Windsurf in order while following the tutorial.

## 1. Set up the project

```
Set up a Python project in this directory following standard Python
packaging conventions:
- Create a virtual environment
- Install httpx==0.28.1 and pytest==9.0.2
- Add a tests/ directory
- Use the directory name as the package name
- Only include the dependencies explicitly listed here
```

## 2. Write the async fetch function

```
Create a file called `fetcher.py` and write an async function
called fetch_json that:
- Takes a URL string and an optional integer max_retries (default 3)
- Uses httpx.AsyncClient to fetch JSON from the URL
- Retries up to max_retries times with exponential backoff (1s, 2s, 4s)
  on any httpx.HTTPError
- Returns the JSON response as a typed dataclass called FetchResult
  with fields: url (str), status_code (int), and data (dict)
- Uses proper type hints throughout
```

## 3. Generate tests

Before sending this prompt, open `fetcher.py` and replace
`await asyncio.sleep(delay)` with `time.sleep(delay)`, then add
`import time` at the top. Save the file.

```
Create tests/test_fetcher.py with pytest tests for fetch_json that:
- Test successful fetch returns correct FetchResult
- Test fetch retries twice then succeeds
- Test fetch raises after exhausting retries
- Test two concurrent fetches complete in <4s
  (one with 1s+2s retry delays, one instant)
- Test fetch can be cancelled during retry delay
Use httpx.MockTransport for mocking.
```

## 4. Plan-mode prompt

Switch each editor to its Plan mode before sending:

```
Add a retry_budget parameter to fetch_json that limits the total
cumulative wait time across all retries.
```

## 5. Autocomplete starter snippet

Type this into a file and let each editor complete it:

```python
@dataclass
class RetryMetadata:
    attempts_made:
# ...
```

## 6. Manual review (Windsurf Ask mode)

```
Review fetcher.py for bugs and lint issues and summarize what you find.
```
