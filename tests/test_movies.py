import pytest

from moviecenter import movies
from moviecenter.movies import Movie


@pytest.fixture
def test_movie_1() -> Movie:
    return Movie(name='LoTR', director='Steve', budget=100000000)


@pytest.fixture
def test_movie_2() -> Movie:
    return Movie(name='Batman v Superman', director='Zack', budget=100000000)


@pytest.fixture
def test_movies(test_movie_1, test_movie_2) -> list[Movie]:
    return [test_movie_1, test_movie_2]


@pytest.fixture
def populate_db(test_movies):
    movies.movies = test_movies


@pytest.mark.asyncio
async def test_get_all_movies(populate_db, test_movies):
    assert await movies.get_all_movies() == test_movies


@pytest.mark.asyncio
async def test_get_movie_by_name_exists(populate_db, test_movie_1):
    assert await movies.get_movie_by_name(test_movie_1.name) == test_movie_1


@pytest.mark.asyncio
async def test_get_movie_by_name_not_exists(populate_db):
    assert await movies.get_movie_by_name('random') is None
