import asyncio
import os
import sys
from pathlib import Path

from copilot import CopilotClient
from copilot.rpc import PermissionDecisionApproveOnce, PermissionDecisionReject

TARGET = sys.argv[1] if len(sys.argv) > 1 else "project/shopping.py"
ALLOWED = Path(TARGET).resolve()


def is_target(path):
    return Path(path).resolve() == ALLOWED


def policy(request, invocation):
    path = getattr(request, "path", "")
    if request.kind == "read" and is_target(path):
        print(f"[approved] read {path}", file=sys.stderr)
        return PermissionDecisionApproveOnce()
    print(f"[rejected] {request.kind} {path}", file=sys.stderr)
    return PermissionDecisionReject(feedback="CI runs are read-only.")


async def main() -> int:
    async with CopilotClient(
        github_token=os.environ["COPILOT_GITHUB_TOKEN"]
    ) as client:
        session = await client.create_session(on_permission_request=policy)
        reply = await session.send_and_wait(
            f"Review {TARGET} for bugs. Reply with only PASS if it is fine, "
            "or FAIL followed by the problems."
        )
        await session.disconnect()
    verdict = reply.data.content.strip() if reply else "FAIL: no reply"
    print(verdict)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
