import os

from langchain.agents import create_agent
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

from chains.hospital_cypher_chain import hospital_cypher_chain
from chains.hospital_review_chain import reviews_vector_chain
from tools.wait_times import (
    get_current_wait_times,
    get_most_available_hospital,
)

HOSPITAL_AGENT_MODEL = os.getenv("HOSPITAL_AGENT_MODEL")

agent_system_prompt = (
    "You are a helpful assistant for a hospital system. Use the tools "
    "available to you to answer the user's questions about patients, "
    "visits, physicians, hospitals, insurance payers, patient reviews, "
    "and current wait times."
)


def query_reviews(query: str) -> str:
    """Answer questions about patient experiences from their reviews."""
    return reviews_vector_chain.invoke(query)


def query_graph(query: str) -> str:
    """Answer questions by querying the hospital graph database."""
    return hospital_cypher_chain.invoke(query)["result"]


tools = [
    Tool(
        name="Experiences",
        func=query_reviews,
        description="""Useful when you need to answer questions
        about patient experiences, feelings, or any other qualitative
        question that could be answered about a patient using semantic
        search. Not useful for answering objective questions that involve
        counting, percentages, aggregations, or listing facts. Use the
        entire prompt as input to the tool. For instance, if the prompt is
        "Are patients satisfied with their care?", the input should be
        "Are patients satisfied with their care?".
        """,
    ),
    Tool(
        name="Graph",
        func=query_graph,
        description="""Useful for answering questions about patients,
        physicians, hospitals, insurance payers, patient review
        statistics, and hospital visit details. Use the entire prompt as
        input to the tool. For instance, if the prompt is "How many visits
        have there been?", the input should be "How many visits have
        there been?".
        """,
    ),
    Tool(
        name="Waits",
        func=get_current_wait_times,
        description="""Use when asked about current wait times
        at a specific hospital. This tool can only get the current
        wait time at a hospital and does not have any information about
        aggregate or historical wait times. Do not pass the word "hospital"
        as input, only the hospital name itself. For example, if the prompt
        is "What is the current wait time at Jordan Inc Hospital?", the
        input should be "Jordan Inc".
        """,
    ),
    Tool(
        name="Availability",
        func=get_most_available_hospital,
        description="""
        Use when you need to find out which hospital has the shortest
        wait time. This tool does not have any information about aggregate
        or historical wait times. This tool returns a dictionary with the
        hospital name as the key and the wait time in minutes as the value.
        """,
    ),
]

chat_model = ChatOpenAI(model=HOSPITAL_AGENT_MODEL)

hospital_rag_agent_executor = create_agent(
    model=chat_model,
    tools=tools,
    system_prompt=agent_system_prompt,
)
