from crewai import Agent, Task, Crew, LLM
from crewai_tools import ScrapeWebsiteTool

llm = LLM(model="gemini/gemini-2.5-flash")

scrape_tool = ScrapeWebsiteTool()

researcher = Agent(
    role="Python Release Analyst",
    goal="Find the latest Python release information",
    backstory=(
        "You're a developer advocate who tracks Python releases"
        " and summarizes what's new for the community."
    ),
    tools=[scrape_tool],
    llm=llm,
)

writer = Agent(
    role="Tech Blogger",
    goal="Write concise release summaries for a developer audience",
    backstory=(
        "You write clear, engaging blog posts that help developers"
        " stay up to date with the Python ecosystem."
    ),
    llm=llm,
)

research_task = Task(
    description=(
        "Scrape https://www.python.org/downloads/ and report"
        " the latest stable Python version number and its release date"
    ),
    expected_output="The latest Python version number and release date",
    agent=researcher,
)

writing_task = Task(
    description=(
        "Write a one-paragraph announcement based on the Python"
        " release information provided by the research task"
    ),
    expected_output=(
        "A concise one hundred word announcement covering the"
        " latest Python version number and release date"
    ),
    agent=writer,
    context=[research_task],
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True,
)

result = crew.kickoff()
print(result.raw)
