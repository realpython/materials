from fastapi import FastAPI

from agents.hospital_rag_agent import hospital_rag_agent_executor
from models.hospital_rag_query import HospitalQueryInput, HospitalQueryOutput

app = FastAPI(
    title="Hospital Chatbot",
    description="Endpoints for a hospital system graph RAG chatbot",
)


@app.get("/")
async def get_status():
    return {"status": "running"}


@app.post("/hospital-rag-agent")
async def query_hospital_agent(
    query: HospitalQueryInput,
) -> HospitalQueryOutput:
    query_response = await hospital_rag_agent_executor.ainvoke(
        {"messages": [{"role": "user", "content": query.text}]}
    )
    messages = query_response["messages"]

    return HospitalQueryOutput(
        input=query.text,
        output=messages[-1].text,
        intermediate_steps=[str(message) for message in messages],
    )
