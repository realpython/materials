import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

os.environ["TOKENIZERS_PARALLELISM"] = "false"

CHROMA_PATH = "car_review_embeddings"
COLLECTION_NAME = "car_reviews"
MODEL = "gpt-5.6-luna"

load_dotenv()

openai_client = OpenAI()
chroma_client = chromadb.PersistentClient(CHROMA_PATH)
collection = chroma_client.get_collection(name=COLLECTION_NAME)

context = """
You are a customer success employee at a large
 car dealership. Use the following car reviews
 to answer questions: {}
"""

question = """
What's the key to great customer satisfaction
 based on detailed positive reviews?
"""

good_reviews = collection.query(
    query_texts=[question],
    n_results=10,
    include=["documents"],
    where={"Rating": {"$gte": 3}},
)

reviews_str = ",".join(good_reviews["documents"][0])

print("Good reviews: ")
print(reviews_str)
print("###########################################")

good_review_summaries = openai_client.responses.create(
    model=MODEL,
    instructions=context.format(reviews_str),
    input=question,
)

print("AI-Generated summary of good reviews: ")
print(good_review_summaries.output_text)
print("###########################################")

question = """
Which of these poor reviews has the
 worst implications about our dealership?
 Explain why.
"""

poor_reviews = collection.query(
    query_texts=[question],
    n_results=5,
    include=["documents"],
    where={"Rating": {"$lte": 3}},
)

reviews_str = ",".join(poor_reviews["documents"][0])

print("Worst reviews: ")
print(poor_reviews["documents"][0][0])
print("###########################################")

poor_review_analysis = openai_client.responses.create(
    model=MODEL,
    instructions=context.format(reviews_str),
    input=question,
)

print("AI-Generated summary of the single worst review: ")
print(poor_review_analysis.output_text)
print("###########################################")
