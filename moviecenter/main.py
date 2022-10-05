from fastapi import FastAPI, HTTPException

from .movies import Movie, get_all_movies, get_movie_by_name

app = FastAPI()


@app.get("/movies", response_model=list[Movie])
async def get_all_movies_api() -> list[Movie]:
    return await get_all_movies()


@app.get("/movies/{name}", response_model=Movie)
async def get_movie_by_name_api(name: str) -> Movie:
    movie = await get_movie_by_name(name)
    if movie is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return movie
