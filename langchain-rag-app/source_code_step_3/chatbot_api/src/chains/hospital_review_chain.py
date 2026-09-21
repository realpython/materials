import logging
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.runnables import RunnablePassthrough
from langchain_neo4j import Neo4jVector
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

# Silence Neo4j's deprecation notice for db.index.vector.queryNodes
logging.getLogger("neo4j.notifications").setLevel(logging.ERROR)

HOSPITAL_QA_MODEL = os.getenv("HOSPITAL_QA_MODEL")

neo4j_vector_index = Neo4jVector.from_existing_graph(
    embedding=OpenAIEmbeddings(),
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="reviews",
    node_label="Review",
    text_node_properties=[
        "physician_name",
        "patient_name",
        "text",
        "hospital_name",
    ],
    embedding_node_property="embedding",
)

review_template = """Your job is to use patient
reviews to answer questions about their experience at a hospital. Use
the following context to answer questions. Be as detailed as possible,
but don't make up any information that's not from the context. If you
don't know an answer, say you don't know.
{context}
"""

review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["context"], template=review_template
    )
)

review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["question"], template="{question}")
)
messages = [review_system_prompt, review_human_prompt]

review_prompt = ChatPromptTemplate(
    input_variables=["context", "question"], messages=messages
)

reviews_retriever = neo4j_vector_index.as_retriever(search_kwargs={"k": 12})
review_chat_model = ChatOpenAI(model=HOSPITAL_QA_MODEL)

reviews_vector_chain = (
    {"context": reviews_retriever, "question": RunnablePassthrough()}
    | review_prompt
    | review_chat_model
    | StrOutputParser()
)
