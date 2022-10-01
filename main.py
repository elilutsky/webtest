from typing import List

from fastapi import FastAPI

app = FastAPI()

movies: List[dict] = [
    {
        'name': 'Matrix',
        'director': 'Steve',
        'budget': 100000000,
    },
    {
        'name': 'The Batman',
        'director': 'Max',
        'budget': 900000000,
    },

]


@app.get("/")
async def root():
    return 'Hello'


@app.get("/movies")
async def get_movies() -> List[dict]:
    return movies
