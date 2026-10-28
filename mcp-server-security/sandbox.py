"""Launch a stdio MCP server inside a bubblewrap sandbox."""

import sys
from pathlib import Path

from mcp import StdioServerParameters

HERE = Path(__file__).parent.resolve()


def sandboxed_params(script: str) -> StdioServerParameters:
    python = Path(sys.executable)  # The venv's interpreter, not resolved
    python_dirs = {sys.base_prefix}
    link = python
    while link.is_symlink():  # Follow each link to the real interpreter
        link = link.parent / link.readlink()
        python_dirs.add(str(link.parents[1]))
    python_binds = []
    for folder in sorted(python_dirs):
        python_binds += ["--ro-bind", folder, folder]
    args = [
        *("--unshare-all", "--die-with-parent", "--clearenv"),
        "--new-session",
        *("--ro-bind", "/usr", "/usr"),
        *("--symlink", "usr/bin", "/bin"),
        *("--symlink", "usr/lib", "/lib"),
        *("--symlink", "usr/lib64", "/lib64"),
        *("--proc", "/proc"),
        *("--tmpfs", "/tmp"),
        *python_binds,
        *("--ro-bind", sys.prefix, sys.prefix),
        *("--ro-bind", str(HERE / script), f"/app/{script}"),
        *("--ro-bind", str(HERE / "workspace"), "/app/workspace"),
        *("--remount-ro", "/"),
        *("--chdir", "/app"),
        *("--setenv", "PATH", "/usr/bin"),
        *(str(python), f"/app/{script}"),
    ]
    return StdioServerParameters(command="bwrap", args=args)
