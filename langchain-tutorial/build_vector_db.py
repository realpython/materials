import csv

import dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


def load_reviews(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def build_documents(reviews):
    documents = []
    for index, review in enumerate(reviews):
        page_content = "\n".join(
            f"{column}: {value}" for column, value in review.items()
        )
        doc = Document(
            page_content=page_content,
            metadata={"source": review["review_id"], "row": index},
        )
        documents.append(doc)
    return documents


def main():
    dotenv.load_dotenv()
    reviews = load_reviews("reviews.csv")
    documents = build_documents(reviews)
    Chroma.from_documents(
        documents,
        OpenAIEmbeddings(model="text-embedding-3-small"),
        persist_directory="chroma_data",
    )


if __name__ == "__main__":
    main()
