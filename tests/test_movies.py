import pytest

from moviecenter import movies
from moviecenter.movies import Movie


@pytest.fixture
def test_movie_1() -> Movie:
    return Movie(name="LoTR", director="Steve", budget=1e6)


@pytest.fixture
def test_movie_2() -> Movie:
    return Movie(name="Batman v Superman", director="Zack", budget=1e7)


@pytest.fixture
def test_movie_new() -> Movie:
    return Movie(name="Justice Leage", director="Zack", budget=1e8)


@pytest.fixture
def test_movies(test_movie_1: Movie, test_movie_2: Movie) -> list[Movie]:
    return [test_movie_1, test_movie_2]


@pytest.fixture(autouse=True)
def populate_db(test_movies: list[Movie]) -> None:
    movies.movies = test_movies


@pytest.mark.asyncio
async def test_get_all_movies(test_movies: Movie) -> None:
    assert await movies.get_all_movies() == test_movies


@pytest.mark.asyncio
async def test_get_movie_by_name_exists(test_movie_1: Movie) -> None:
    assert await movies.get_movie_by_name(test_movie_1.name) == test_movie_1


@pytest.mark.asyncio
async def test_get_movie_by_name_not_exists() -> None:
    assert await movies.get_movie_by_name("random") is None


@pytest.mark.asyncio
async def test_add_movie(test_movie_new: Movie) -> None:
    await movies.add_movie(test_movie_new)

    assert await movies.get_movie_by_name(test_movie_new.name) == test_movie_new


@pytest.mark.asyncio
async def test_delete_movie(test_movie_1: Movie) -> None:
    await movies.delete_movie(test_movie_1)

    assert await movies.get_movie_by_name(test_movie_1.name) is None
