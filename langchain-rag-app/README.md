# Build an LLM RAG Chatbot With LangChain

This repo contains the source code for [Build an LLM RAG Chatbot With LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/)

To run the final application that you'll build in this tutorial, you can use the code provided in `source_code_final/`.

## Project Layout

Each folder holds the code as it stands at the end of the matching step in the tutorial:

| Folder | Tutorial step |
| --- | --- |
| `data/` | The hospital system CSV files used throughout the tutorial |
| `source_code_step_1/` | Step 1: Understand the Business Requirements and Data |
| `source_code_step_2/` | Step 2: Set Up a Neo4j Graph Database |
| `source_code_step_3/` | Step 3: Build a Graph RAG Chatbot in LangChain |
| `source_code_step_4/` | Step 4: Deploy the LangChain Agent |
| `source_code_final/` | The finished application |

The LangChain basics that this tutorial builds on live in a separate tutorial, [LangChain Tutorial: Build Your First Chains and Agents](https://realpython.com/langchain-tutorial/), along with its own sample code.

## Setup

Create a `.env` file in the root directory and add the following environment variables:

```.env
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>

NEO4J_URI=<YOUR_NEO4J_URI>
NEO4J_USERNAME=<YOUR_NEO4J_USERNAME>
NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>

HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/realpython/materials/refs/heads/master/langchain-rag-app/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/realpython/materials/refs/heads/master/langchain-rag-app/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/realpython/materials/refs/heads/master/langchain-rag-app/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/realpython/materials/refs/heads/master/langchain-rag-app/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/realpython/materials/refs/heads/master/langchain-rag-app/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/realpython/materials/refs/heads/master/langchain-rag-app/data/reviews.csv

HOSPITAL_AGENT_MODEL=gpt-5.6-luna
HOSPITAL_CYPHER_MODEL=gpt-5.6-luna
HOSPITAL_QA_MODEL=gpt-5.6-luna

CHATBOT_URL=http://chatbot_api:8000/hospital-rag-agent
```

The chatbot uses OpenAI LLMs, so you'll need to create an [OpenAI API key](https://realpython.com/generate-images-with-dalle-openai-api/#get-your-openai-api-key) and store it as `OPENAI_API_KEY`. 

The three `NEO4J_` variables configure the Neo4j Community Edition instance that Docker Compose runs for you, so there's no cloud account to set up. Point `NEO4J_URI` at the Bolt endpoint on your machine, use the default `neo4j` user, and choose your own password of at least eight characters. Compose reads `NEO4J_PASSWORD` when it creates the database container, and the ETL and chatbot services reach Neo4j over the Compose network instead of `localhost`.

Keep your real credentials in `.env` only. That file is listed in `.gitignore`, so it stays out of version control.

Once you've filled in all of the environment variables and installed [Docker Compose](https://docs.docker.com/compose/install/), open a terminal and run:

```console
$ docker compose up --build
```

After each container finishes building, you'll be able to access the chatbot API at `http://localhost:8000/docs` and the Streamlit app at `http://localhost:8501/`.
