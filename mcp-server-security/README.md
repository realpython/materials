# MCP Server Security: How to Harden a Python MCP Server

This folder provides the code examples for the Real Python tutorial
[MCP Server Security: How to Harden a Python MCP Server](https://realpython.com/mcp-server-security/).
Everything is a harmless local simulation: the "secrets" are fake and no
network access is needed.

## Setup

```console
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Python 3.11 or later is required. The sandbox demos need
[Bubblewrap](https://github.com/containers/bubblewrap) (`bwrap`) on Linux.

## Run

```console
(venv) $ python scan_server.py "$(which python)" vulnerable_server.py
(venv) $ python attack_demo.py "$(which python)" vulnerable_server.py
(venv) $ python sandbox_demo.py
(venv) $ python audience_demo.py
(venv) $ python checklist.py
```

- `vulnerable_server.py`: a server with a poisoned description, an
  over-broad shell tool, and unrestricted file reads
- `scan_server.py`: lists a server's tools and flags risky metadata
- `attack_demo.py`: plays an agent that obeyed the poisoned description
- `hardened_server.py`: narrow tools plus bearer-token auth over HTTP
- `sandbox.py` and `sandbox_demo.py`: run a server inside `bwrap`
- `audience_demo.py`: a token for another server, with and without the
  audience check
- `checklist.py`: before and after results for every check
