import argparse
import pathlib


def parse_args():
    """Parse command line arguments and return parsed args."""
    parser = argparse.ArgumentParser(description="A minimal MCP client")
    parser.add_argument(
        "server_path",
        type=pathlib.Path,
        help="path to the MCP server script",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--members",
        action="store_true",
        help="list the MCP server's tools, prompts, and resources",
    )
    group.add_argument(
        "--chat",
        action="store_true",
        help="start an AI-powered chat with MCP server integration",
    )
    return parser.parse_args()
