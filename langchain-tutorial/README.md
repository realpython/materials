# LangChain Tutorial: From Prompts to RAG and AI Agents

This folder provides the code examples for the Real Python tutorial [LangChain Tutorial: From Prompts to RAG and AI Agents](https://realpython.com/langchain-tutorial/).

## Files

- `build_vector_db.py`: Loads `reviews.csv` into a ChromaDB vector database in `chroma_data/`
- `rag.py`: Answers questions about the patient reviews with a RAG chain
- `agents.py`: Answers exact lookup questions with a tool-calling agent
- `reviews.csv`: Synthetic patient reviews used in the RAG and agent sections

## Setup

Create and activate a virtual environment with Python 3.10 or later, and then install the dependencies:

```console
(venv) $ python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your OpenAI API key:

```dotenv
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

## Usage

Run the scripts from this folder. First, build the vector database:

```console
(venv) $ python build_vector_db.py
```

Then, ask the RAG app about the reviews:

```console
(venv) $ python rag.py "Has anyone complained about communication with staff?"
```

Or ask the agent a lookup question:

```console
(venv) $ python agents.py "How many reviews does Laura Brown's hospital have?"
```
