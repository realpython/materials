"""The same notes server, hardened: narrow tools, bearer auth, audience."""

import hmac
import os
from pathlib import Path

from mcp.server.auth.middleware.auth_context import get_access_token
from mcp.server.auth.provider import AccessToken
from mcp.server.auth.settings import AuthSettings
from mcp.server.mcpserver import MCPServer

HOST, PORT = "127.0.0.1", 8765
RESOURCE_URL = f"http://{HOST}:{PORT}/mcp"
WORKSPACE = Path(__file__).parent.joinpath("workspace").resolve()
MAX_NOTE_CHARS = 200

# Tokens come from the environment, never from tool arguments or code.
# In production an authorization server issues them; this maps each one
# to the resource (audience) it was minted for.
TOKENS = {
    os.environ.get("NOTES_TOKEN", ""): ("notes-client", RESOURCE_URL),
    os.environ.get("OTHER_SERVER_TOKEN", ""): (
        "notes-client",
        "http://127.0.0.1:9000/mcp",
    ),
}


class StaticTokenVerifier:
    async def verify_token(self, token: str) -> AccessToken | None:
        for known, (client_id, resource) in TOKENS.items():
            if known and hmac.compare_digest(known.encode(), token.encode()):
                return AccessToken(
                    token=token,
                    client_id=client_id,
                    scopes=["notes:read", "notes:write"],
                    resource=resource,
                )
        return None


mcp = MCPServer(
    "notes-helper",
    token_verifier=StaticTokenVerifier(),
    auth=AuthSettings(
        issuer_url="http://127.0.0.1:9999",
        resource_server_url=RESOURCE_URL,
        required_scopes=["notes:read"],
        validate_token_resource=os.environ.get("VALIDATE_AUDIENCE", "1")
        == "1",
    ),
)


def safe_path(name: str) -> Path:
    """Resolve name inside WORKSPACE or raise ValueError."""
    path = (WORKSPACE / name).resolve()
    if not path.is_relative_to(WORKSPACE) or path.suffix != ".txt":
        raise ValueError("Only .txt notes inside the workspace are allowed")
    return path


@mcp.tool()
def read_note(name: str) -> str:
    """Read a .txt note from the notes workspace."""
    return safe_path(name).read_text(encoding="utf-8")


@mcp.tool()
def add_note(name: str, text: str) -> str:
    """Save a short note as a .txt file in the notes workspace."""
    token = get_access_token()
    if token is None or "notes:write" not in token.scopes:
        raise ValueError("Missing scope: notes:write")
    if len(text) > MAX_NOTE_CHARS:
        raise ValueError(f"Note longer than {MAX_NOTE_CHARS} characters")
    with safe_path(name).open("x", encoding="utf-8") as file:
        file.write(text)
    return f"Saved {name}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host=HOST, port=PORT)
