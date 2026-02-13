import requests
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


class UserDatabase:
    """Simulate a user database using the JSONPlaceholder users API."""

    _base_url = "https://jsonplaceholder.typicode.com"

    def get_user_info(self, user_id: int) -> dict:
        response = requests.get(f"{self._base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()


class UserSummary(BaseModel):
    name: str
    email: str
    company: str


agent = Agent(
    "google-gla:gemini-2.5-flash",
    output_type=UserSummary,
    deps_type=UserDatabase,
    system_prompt=(
        "You retrieve user information from an external database. "
        "Use the available tools to gather user info, "
        "then return a structured summary."
    ),
)


@agent.tool
def fetch_user(ctx: RunContext[UserDatabase], user_id: int) -> str:
    """Fetch user profile from the service."""
    try:
        user = ctx.deps.get_user_info(user_id)
        return str(user)
    except requests.HTTPError:
        return f"User with ID {user_id} not found"


db = UserDatabase()
result = agent.run_sync(
    "Get a summary for user 7",
    deps=db,
)  # Inject the database
print(f"Name: {result.output.name}")
print(f"Email: {result.output.email}")
print(f"Company: {result.output.company}")
