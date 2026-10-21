from mcp.server import MCPServer
from tool import get_package_info

mcp = MCPServer("pypi-tools")
mcp.add_tool(get_package_info)

if __name__ == "__main__":
    mcp.run()
