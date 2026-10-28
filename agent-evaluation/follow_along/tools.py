"""Tools for the helpdesk agent: a package registry and a docs search."""

import json

REGISTRY = {
    "billing-client": {
        "latest": "3.2.0",
        "python": ">=3.11",
        "owner": "Payments",
    },
    "auth-client": {
        "latest": "1.8.1",
        "python": ">=3.10",
        "owner": "Identity",
    },
    "metrics-client": {
        "latest": "0.9.4",
        "python": ">=3.10",
        "owner": "Platform",
    },
}

DOCS = {
    "billing-client-overview": (
        "billing-client: current release is 2.4. Supports Python 3.9 "
        "and later. (This page is out of date.)"
    ),
    "auth-client-install": (
        "Install auth-client from the team index with: "
        "pip install --index-url https://pypi.internal.example/simple "
        "auth-client"
    ),
    "metrics-client-batching": (
        "metrics-client batching: call Batcher(flush_every=50) to send "
        "metrics in groups of 50 instead of one request per metric."
    ),
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_package",
            "description": (
                "Look up a package in the team registry. Returns its "
                "latest version, supported Python versions, and owner."
            ),
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": (
                "Keyword search over the internal documentation pages."
            ),
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
]


def lookup_package(name: str) -> str:
    info = REGISTRY.get(name.lower())
    if info is None:
        return f"{name}: not found in the registry"
    return (
        f"{name}: latest {info['latest']}, Python {info['python']}, "
        f"owner {info['owner']}"
    )


def search_docs(query: str) -> str:
    words = query.lower().split()
    hits = [
        f"[{page}] {text}"
        for page, text in DOCS.items()
        if any(word in f"{page} {text}".lower() for word in words)
    ]
    return "\n".join(hits) or "no matching pages"


def call_tool(name: str, arguments: dict) -> str:
    functions = {
        "lookup_package": lookup_package,
        "search_docs": search_docs,
    }
    if name not in functions:
        return json.dumps({"error": f"unknown tool {name}"})
    return functions[name](**arguments)
