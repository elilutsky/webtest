from fastapi import APIRouter, HTTPException, Request

from .movies import Movie, add_movie, delete_movie, get_all_movies, get_movie_by_name

movies_router = APIRouter()


@movies_router.get("/movies", response_model=list[Movie])
async def get_all_movies_api(request: Request) -> list[Movie]:
    return await get_all_movies(request.app.state.db)


@movies_router.get("/movies/{name}", response_model=Movie)
async def get_movie_by_name_api(request: Request, name: str) -> Movie:
    movie = await get_movie_by_name(request.app.state.db, name)
    if movie is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return movie


@movies_router.post("/movies")
async def add_movie_api(request: Request, movie: Movie) -> None:
    await add_movie(request.app.state.db, movie)


@movies_router.delete("/movies/{name}")
async def delete_movie_api(request: Request, name: str) -> None:
    await delete_movie(request.app.state.db, name)
