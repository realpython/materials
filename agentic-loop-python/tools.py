"""Tools the agent can call during its loop."""

import subprocess


TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "run_tests",
            "description": (
                "Run the pytest suite on test_search.py and return the output."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "reasoning": {
                        "type": "string",
                        "description": (
                            "One short sentence explaining "
                            "why you're running the tests "
                            "now."
                        ),
                    },
                },
                "required": ["reasoning"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_benchmark",
            "description": (
                "Benchmark search_similar() and return the elapsed time."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "reasoning": {
                        "type": "string",
                        "description": (
                            "One short sentence explaining "
                            "why you're running the "
                            "benchmark now."
                        ),
                    },
                },
                "required": ["reasoning"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_code",
            "description": ("Read and return a Python file's contents."),
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "File to read.",
                    },
                    "reasoning": {
                        "type": "string",
                        "description": (
                            "One short sentence explaining "
                            "why you're reading this file "
                            "now."
                        ),
                    },
                },
                "required": ["filename", "reasoning"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_code",
            "description": ("Overwrite a Python file with new code."),
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": ("File to write."),
                    },
                    "content": {
                        "type": "string",
                        "description": ("The new file contents."),
                    },
                    "reasoning": {
                        "type": "string",
                        "description": (
                            "One short sentence explaining "
                            "what this change does and "
                            "why."
                        ),
                    },
                },
                "required": [
                    "filename",
                    "content",
                    "reasoning",
                ],
            },
        },
    },
]

OPTIMIZATION_MENU = (
    "Available optimization techniques:\n"
    "1. Set/dict swap: Replace list lookups "
    "with set lookups\n"
    "2. Built-in replacement: Use built-ins "
    "instead of loops\n"
    "3. functools.cache: Cache repeated "
    "function calls\n"
    "4. NumPy vectorization: Replace Python "
    "loops with NumPy array operations"
)


def run_tests():
    """Run pytest and return the captured output."""
    result = subprocess.run(
        [
            "python",
            "-m",
            "pytest",
            "test_search.py",
            "-v",
        ],
        capture_output=True,
        text=True,
    )
    return result.stdout + result.stderr


def run_benchmark():
    """Time search_similar() and return the result."""
    setup = (
        "from search import load_vectors, "
        "search_similar; "
        "stored = load_vectors(500, 128); "
        "query = stored[0]"
    )
    result = subprocess.run(
        [
            "python",
            "-m",
            "timeit",
            "-n",
            "10",
            "-r",
            "3",
            "-s",
            setup,
            "search_similar(query, stored)",
        ],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def read_code(filename):
    """Read and return the contents of a file."""
    with open(filename) as f:
        return f.read()


def write_code(filename, content):
    """Write new contents to a file."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Wrote {len(content)} characters to {filename}"


TOOL_REGISTRY = {
    "run_tests": run_tests,
    "run_benchmark": run_benchmark,
    "read_code": read_code,
    "write_code": write_code,
}
