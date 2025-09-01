from fastapi import FastAPI

app = FastAPI()

items_db = []


@app.get("/")
def home():
    return {"message": "Welcome to the Randomizer API"}
