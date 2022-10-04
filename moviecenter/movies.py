from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    director: str
    budget: int


movies: list[Movie] = [
    Movie(name='Matrix', director='Steve', budget=100000000),
    Movie(name='The Batman', director='Max', budget=900000000)
]


async def get_all_movies() -> list[Movie]:
    return movies


async def get_movie_by_name(name: str) -> Movie | None:
    return next(filter(lambda movie: movie.name == name, await get_all_movies()), None)

