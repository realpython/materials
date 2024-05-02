from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict

from crud_sql_alchemy import Bird, init_db
from crud_sql_alchemy import Session as SessionLocal

app = FastAPI()
init_db()


class BirdCreate(BaseModel):
    name: str


class BirdUpdate(BaseModel):
    name: str


class BirdResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/birds/", response_model=BirdResponse)
def create_bird(bird: BirdCreate, db: Session = Depends(get_db)):
    new_bird = Bird(name=bird.name)
    db.add(new_bird)
    db.commit()
    db.refresh(new_bird)
    return new_bird


@app.get("/birds/", response_model=list[BirdResponse])
def read_birds(db: Session = Depends(get_db)):
    birds = db.execute(select(Bird)).scalars().all()
    return birds


@app.get("/birds/{bird_id}", response_model=BirdResponse)
def read_bird(bird_id: int, db: Session = Depends(get_db)):
    query = select(Bird).where(Bird.id == bird_id)
    found_bird = db.execute(query).scalar_one()
    if found_bird is None:
        raise HTTPException(status_code=404, detail="Bird not found")
    return found_bird


@app.put("/birds/{bird_id}", response_model=BirdResponse)
def update_bird(bird_id: int, bird: BirdUpdate, db: Session = Depends(get_db)):
    query = select(Bird).where(Bird.id == bird_id)
    found_bird = db.execute(query).scalar_one()
    if found_bird is None:
        raise HTTPException(status_code=404, detail="Bird not found")
    found_bird.name = bird.name
    db.commit()
    db.refresh(found_bird)
    return found_bird


@app.delete("/birds/{bird_id}", response_model=dict)
def delete_bird(bird_id: int, db: Session = Depends(get_db)):
    query = select(Bird).where(Bird.id == bird_id)
    found_bird = db.execute(query).scalar_one()
    if found_bird is None:
        raise HTTPException(status_code=404, detail="Bird not found")
    db.delete(found_bird)
    db.commit()
    return {"message": "Bird deleted successfully"}
