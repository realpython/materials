from pydantic_ai import Agent

agent = Agent(
    "google-gla:gemini-2.5-flash",
    system_prompt="You're a Python Expert. Reply in one sentence.",
)

result = agent.run_sync("What is Pydantic AI?")
print(result.output)
