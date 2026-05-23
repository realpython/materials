from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(model="gemini/gemini-2.5-flash")

researcher = Agent(
    role="Senior Research Analyst",
    goal="Find comprehensive information about a given topic",
    backstory=(
        "You're a seasoned research analyst with a knack for"
        " uncovering the most relevant and accurate information."
        " You're known for your thorough and well-organized research."
    ),
    llm=llm,
)

writer = Agent(
    role="Content Writer",
    goal="Write clear, engaging content based on research findings",
    backstory=(
        "You're an experienced writer who excels at transforming"
        " complex research into accessible, well-structured articles"
        " that readers enjoy."
    ),
    llm=llm,
)

research_task = Task(
    description="Research the latest trends in renewable energy technology",
    expected_output=(
        "A detailed list of the top five renewable energy trends" " with explanations"
    ),
    agent=researcher,
)

writing_task = Task(
    description="Write a short article based on the research findings",
    expected_output=(
        "A well-structured article of about three hundred words"
        " on renewable energy trends"
    ),
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print(result.raw)
