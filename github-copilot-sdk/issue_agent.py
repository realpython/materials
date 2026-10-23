import asyncio
import json
import os
from pathlib import Path
from typing import Literal

from copilot import CopilotClient, PermissionHandler, define_tool
from pydantic import BaseModel, Field

ISSUES = json.loads(
    Path(__file__).with_name("tracker").joinpath("issues.json").read_text()
)


class ListIssuesParams(BaseModel):
    status: Literal["open", "closed"] = Field(
        description="Filter by status: 'open' or 'closed'"
    )
    label: str | None = Field(
        default=None, description="Optional label to filter by"
    )


@define_tool(
    description="List issues from the tracker", params_type=ListIssuesParams
)
async def list_issues(params: ListIssuesParams):
    return [
        issue
        for issue in ISSUES
        if issue["status"] == params.status
        and (params.label is None or params.label in issue["labels"])
    ]


async def main():
    async with CopilotClient(
        github_token=os.environ["COPILOT_GITHUB_TOKEN"]
    ) as client:
        session = await client.create_session(
            tools=[list_issues],
            on_permission_request=PermissionHandler.approve_all,
        )
        reply = await session.send_and_wait(
            "Which open bugs are assigned to ana? Use the tracker tool."
        )
        print(reply.data.content)
        await session.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
