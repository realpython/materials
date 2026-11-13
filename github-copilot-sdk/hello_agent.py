import asyncio
import os

from copilot import CopilotClient, PermissionHandler


async def main():
    token = os.environ["COPILOT_GITHUB_TOKEN"]
    async with CopilotClient(github_token=token) as client:
        session = await client.create_session(
            on_permission_request=PermissionHandler.approve_all,
            model="claude-haiku-5.5",
        )
        reply = await session.send_and_wait(
            "What is the walrus operator in Python? One sentence."
        )
        print(reply.data.content)
        await session.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
