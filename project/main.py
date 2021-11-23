from typing import Optional

from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine

from .abstractions import MultipleModels, GenerateEndpoints


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None


class HeroRead(HeroBase):
    id: int


hero_models = MultipleModels(path="/heroes/", base=HeroBase, response=HeroRead)
Hero = hero_models.table  # Shim to avoid changing tests.

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()

hero_endpoints = GenerateEndpoints(app, get_session, hero_models)
