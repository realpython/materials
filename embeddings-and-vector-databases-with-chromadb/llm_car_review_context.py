import json
import os

import chromadb
import openai
from chromadb.utils import embedding_functions

os.environ["TOKENIZERS_PARALLELISM"] = "false"

DATA_PATH = "data/archive/*"
CHROMA_PATH = "car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"

with open("config.json", "r") as json_file:
    config_data = json.load(json_file)

openai.api_key = config_data.get("openai-secret-key")

client = chromadb.PersistentClient(CHROMA_PATH)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_FUNC_NAME
)

collection = client.get_collection(
    name=COLLECTION_NAME, embedding_function=embedding_func
)

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

good_review_summaries = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": context.format(reviews_str)},
        {"role": "user", "content": question},
    ],
    temperature=0,
    n=1,
)

reviews_str = ",".join(good_reviews["documents"][0])

print("Good reviews: ")
print(reviews_str)
print("###########################################")

good_review_summaries = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": context.format(reviews_str)},
        {"role": "user", "content": question},
    ],
    temperature=0,
    n=1,
)

print("AI-Generated summary of good reviews: ")
print(good_review_summaries["choices"][0]["message"]["content"])
print("###########################################")


context = """
          You are a customer success employee at a large car dealership.
          Use the following car reivews to answer questions: {}
          """
question = """
            Which of these poor reviews has the worst implications about
            our dealership? Explain why.
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

poor_review_analysis = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": context.format(reviews_str)},
        {"role": "user", "content": question},
    ],
    temperature=0,
    n=1,
)

print("AI-Generated summary of the single worst review: ")
print(poor_review_analysis["choices"][0]["message"]["content"])
print("###########################################")
