from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Bird(Base):
    __tablename__ = "bird"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Bird(id={self.id}, name={self.name!r})"


engine = create_engine("sqlite:///birds.db")
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
