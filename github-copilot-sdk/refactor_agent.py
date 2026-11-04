import asyncio
import os
import shutil
import tempfile
from pathlib import Path

from copilot import CopilotClient, PermissionHandler, SessionEventType

PROJECT = Path(__file__).with_name("project")


def on_event(event):
    match event.type:
        case SessionEventType.ASSISTANT_MESSAGE_DELTA:
            print(event.data.delta_content, end="", flush=True)
        case SessionEventType.TOOL_EXECUTION_START:
            print(f"\n[tool start] {event.data.tool_name}")
        case SessionEventType.TOOL_EXECUTION_COMPLETE:
            print(f"[tool done] success={event.data.success}")
        case SessionEventType.SESSION_IDLE:
            print("\n[idle]")


async def main():
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "project"
        shutil.copytree(PROJECT, workdir)
        print(f"Working in {workdir}")
        async with CopilotClient(
            github_token=os.environ["COPILOT_GITHUB_TOKEN"]
        ) as client:
            session = await client.create_session(
                streaming=True,
                working_directory=str(workdir),
                on_permission_request=PermissionHandler.approve_all,
            )
            session.on(on_event)
            await session.send_and_wait(
                "In shopping.py, make total() use sum() and make average() "
                "return 0 for an empty list. Don't touch the tests."
            )
            await session.disconnect()
        print((workdir / "shopping.py").read_text())


if __name__ == "__main__":
    asyncio.run(main())
