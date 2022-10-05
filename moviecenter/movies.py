from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    director: str
    budget: int


movies: list[Movie] = [
    Movie(name="Matrix", director="Steve", budget=100000000),
    Movie(name="The Batman", director="Max", budget=900000000),
]


async def get_all_movies() -> list[Movie]:
    return movies


async def get_movie_by_name(name: str) -> Movie | None:
    return next((m for m in await get_all_movies() if m.name == name), None)


async def add_movie(movie: Movie) -> None:
    movies.append(movie)


async def delete_movie(movie: Movie) -> None:
    movies.remove(movie)
