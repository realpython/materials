from crewai import Agent, Task, Crew, LLM

llm = LLM(model="gemini/gemini-2.5-flash")

travel_agent = Agent(
    role="Travel Advisor",
    goal="Provide helpful travel recommendations",
    backstory=(
        "You're an experienced travel advisor who has visited"
        " over fifty countries and specializes in budget-friendly"
        " adventure travel."
    ),
    llm=llm,
    verbose=True,
)

task = Task(
    description="Suggest three budget-friendly destinations in Southeast Asia",
    expected_output="A short list of three destinations with brief descriptions",
    agent=travel_agent,
)

crew = Crew(agents=[travel_agent], tasks=[task])
result = crew.kickoff()
print(result.raw)
