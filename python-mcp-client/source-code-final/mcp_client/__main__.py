import asyncio

from mcp_client.cli import parse_args
from mcp_client.mcp_client import MCPClient


def main():
    """Entry point for the mcp-client CLI app."""
    args = parse_args()
    if not args.server_path.exists():
        print(f"Error: Server script '{args.server_path}' not found")
        return

    async def run():
        try:
            async with MCPClient(args.server_path) as client:
                if args.members:
                    await client.list_all_members()
                elif args.chat:
                    await client.run_chat()
        except RuntimeError as e:
            print(e)

    asyncio.run(run())


if __name__ == "__main__":
    main()
