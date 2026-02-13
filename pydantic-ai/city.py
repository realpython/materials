from pydantic import BaseModel
from pydantic_ai import Agent


class CityInfo(BaseModel):
    name: str
    country: str
    population: int
    fun_fact: str


agent = Agent("google-gla:gemini-2.5-flash", output_type=CityInfo)

result = agent.run_sync("Tell me about Tokyo")
print(result.output)


print(f"{result.output.name}, {result.output.country}")
print(f"Population: {result.output.population:,}")
print(f"Fun fact: {result.output.fun_fact}")
