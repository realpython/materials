# MCP vs API Calls: Which Should You Use for Python LLM Apps?

This folder contains the sample code for the Real Python tutorial [MCP vs API Calls: Which Should You Use for Python LLM Apps?](https://realpython.com/mcp-vs-api-calls/).

## Files

- `tool.py`: the PyPI lookup function that both approaches share, written with the standard library only.
- `client_api.py`: the direct API calls integration, which declares the tool schema by hand.
- `server.py`: the MCP server, which exposes the tool through the `mcp` SDK.
- `client.py`: the MCP client, which discovers and calls the tool through the server.

## Setup

Create a virtual environment and install the dependencies:

```console
$ python -m venv tools-venv
$ source tools-venv/bin/activate
(tools-venv) $ python -m pip install anthropic "mcp>=2,<3"
```

The examples use the Anthropic client, which requires an API key. Create a key in the [Anthropic Console](https://console.anthropic.com/), scope it to a single workspace, and export it:

```console
(tools-venv) $ export ANTHROPIC_API_KEY="your-api-key-here"
```

## Running the examples

Run the direct API calls version:

```console
(tools-venv) $ python client_api.py
The latest version of the Jinja2 package is 3.1.6.
```

Run the MCP version:

```console
(tools-venv) $ python client.py
The latest version of the Jinja2 package is 3.1.6.
```

You only run `client.py`. It launches `server.py` as a subprocess and talks to it over standard I/O, so you never start the server yourself.
