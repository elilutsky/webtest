from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    name: str
    director: str
    budget: int


movies: list[Movie] = [
    Movie(name='Matrix', director='Steve', budget=100000000),
    Movie(name='The Batman', director='Max', budget=900000000)
]


@app.get('/')
async def root():
    return 'Hello'


@app.get('/movies')
async def get_movies() -> list[Movie]:
    return movies
