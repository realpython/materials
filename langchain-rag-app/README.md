# Build an LLM RAG Chatbot With LangChain

This repo contains the source code for [Build an LLM RAG Chatbot With LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/)

To run the final application that you'll build in this tutorial, you can use the code provided in `source_code_final/`.

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

HOSPITAL_AGENT_MODEL=gpt-5.5
HOSPITAL_CYPHER_MODEL=gpt-5.5
HOSPITAL_QA_MODEL=gpt-5.5

CHATBOT_URL=http://chatbot_api:8000/hospital-rag-agent
```

The chatbot uses OpenAI LLMs, so you'll need to create an [OpenAI API key](https://realpython.com/generate-images-with-dalle-openai-api/#get-your-openai-api-key) and store it as `OPENAI_API_KEY`. 

The three `NEO4J_` variables are used to connect to your Neo4j AuraDB instance. Follow the directions [here](https://neo4j.com/cloud/platform/aura-graph-database/?ref=docs-nav-get-started) to create a free instance.

Once you have a running Neo4j instance, and have filled out all the environment variables in `.env`, you can run the entire project with [Docker Compose](https://docs.docker.com/compose/). You can install Docker Compose by following [these directions](https://docs.docker.com/compose/install/).

Once you've filled in all of the environment variables, set up a Neo4j AuraDB instance, and installed Docker Compose, open a terminal and run:

```console
$ docker compose up --build
```

After each container finishes building, you'll be able to access the chatbot API at `http://localhost:8000/docs` and the Streamlit app at `http://localhost:8501/`.
