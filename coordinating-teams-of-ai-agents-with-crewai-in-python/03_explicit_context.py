from crewai import Agent, Task, Crew, LLM

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
    description=(
        "Research the current state of electric vehicle adoption"
        " worldwide"
    ),
    expected_output=(
        "A bullet-point list of key statistics and trends"
        " in EV adoption"
    ),
    agent=researcher,
)

writing_task = Task(
    description=(
        "Using the provided research, write a concise summary article"
        " about electric vehicle adoption"
    ),
    expected_output="A two hundred word article summarizing EV adoption trends",
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