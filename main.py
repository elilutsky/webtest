from fastapi import FastAPI

from movies import Movie, get_all_movies

app = FastAPI()


@app.get('/')
async def root():
    return 'Hello'


@app.get('/movies')
async def get_movies() -> list[Movie]:
    return await get_all_movies()
