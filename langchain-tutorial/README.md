# LangChain Tutorial: Build Your First Chains and Agents

Sample code for the Real Python tutorial [LangChain Tutorial: Build Your First Chains and Agents](https://realpython.com/langchain-tutorial/).

This is the `langchain_intro` project you build throughout the tutorial: a chat model, reusable prompt templates, an LCEL chain, a ChromaDB-backed review retriever (RAG), and a tool-calling agent that answers questions about patient reviews and hospital wait times.

## Project layout

```
langchain-tutorial/
│
├── data/
│   └── reviews.csv
│
├── langchain_intro/
│   ├── chatbot.py            # final chat model + prompt templates + RAG chain + agent
│   ├── create_retriever.py   # builds the ChromaDB vector database from reviews.csv
│   └── tools.py              # get_current_wait_time() tool
│
├── .env.example
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment (Python 3.10 or later), then install the dependencies:

   ```console
   (venv) $ python -m pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your OpenAI API key:

   ```console
   (venv) $ cp .env.example .env
   ```

   ```dotenv
   OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
   ```

3. Build the ChromaDB vector database from the reviews. Run this from the project root; it creates a `chroma_data/` directory with the embedded reviews:

   ```console
   (venv) $ python langchain_intro/create_retriever.py
   ```

## Try it out

Start a Python REPL **from the project root** so the `langchain_intro` package is importable and `dotenv` finds your `.env`:

```pycon
>>> from langchain_intro.chatbot import review_chain
>>> review_chain.invoke("Has anyone complained about communication with the hospital staff?")

>>> from langchain_intro.chatbot import hospital_agent_executor
>>> response = hospital_agent_executor.invoke(
...     {
...         "messages": [
...             {"role": "user", "content": "What is the current wait time at hospital C?"}
...         ]
...     }
... )
>>> response["messages"][-1].text
```
