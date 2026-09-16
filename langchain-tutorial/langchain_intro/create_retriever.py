import csv

import dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

REVIEWS_CSV_PATH = "data/reviews.csv"
REVIEWS_CHROMA_PATH = "chroma_data"

dotenv.load_dotenv()


def load_reviews(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            Document(
                page_content="\n".join(
                    f"{column}: {value}" for column, value in row.items()
                ),
                metadata={"source": row["review"], "row": index},
            )
            for index, row in enumerate(reader)
        ]


reviews = load_reviews(REVIEWS_CSV_PATH)

reviews_vector_db = Chroma.from_documents(
    reviews, OpenAIEmbeddings(), persist_directory=REVIEWS_CHROMA_PATH
)
