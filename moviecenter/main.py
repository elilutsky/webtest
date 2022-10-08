from fastapi import FastAPI, HTTPException

from .movies import (
    Movie,
    MovieMongoClient,
    add_movie,
    delete_movie,
    get_all_movies,
    get_movie_by_name,
)

app = FastAPI()

db_client = MovieMongoClient("mongodb://mongodb:27017")


@app.get("/movies", response_model=list[Movie])
async def get_all_movies_api() -> list[Movie]:
    return await get_all_movies(db_client)


@app.get("/movies/{name}", response_model=Movie)
async def get_movie_by_name_api(name: str) -> Movie:
    movie = await get_movie_by_name(db_client, name)
    if movie is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return movie


@app.post("/movies")
async def add_movie_api(movie: Movie) -> None:
    await add_movie(db_client, movie)


@app.delete("/movies/{name}")
async def delete_movie_api(name: str) -> None:
    await delete_movie(db_client, name)
