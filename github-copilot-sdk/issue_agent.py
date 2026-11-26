import asyncio
import json
import os
from pathlib import Path
from typing import Literal

from copilot import CopilotClient, PermissionHandler, define_tool
from pydantic import BaseModel

ISSUES = json.loads(Path("tracker/issues.json").read_text())


class ListIssuesParams(BaseModel):
    status: Literal["open", "closed"]
    label: str | None = None


@define_tool(description="List issues from the tracker")
async def list_issues(params: ListIssuesParams):
    return [
        issue
        for issue in ISSUES
        if issue["status"] == params.status
        and (params.label is None or params.label in issue["labels"])
    ]


async def main():
    token = os.environ["COPILOT_GITHUB_TOKEN"]
    async with CopilotClient(github_token=token) as client:
        session = await client.create_session(
            tools=[list_issues],
            on_permission_request=PermissionHandler.approve_all,
            model="claude-haiku-5.5",
        )
        reply = await session.send_and_wait(
            "Which open bugs are assigned to Ana? Use the tracker tool."
        )
        print(reply.data.content)
        await session.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
