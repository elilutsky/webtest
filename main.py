from fastapi import FastAPI

from movies import Movie, get_all_movies, get_movie_by_name

app = FastAPI()


@app.get('/')
async def root():
    return 'Hello'


@app.get('/movies', response_model=list[Movie])
async def get_all_movies_api():
    return await get_all_movies()


@app.get('/movies/{name}', response_model=Movie)
async def get_movie_by_name_api(name: str):
    return await get_movie_by_name(name)
