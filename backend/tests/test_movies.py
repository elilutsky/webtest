import os
import typing
from typing import Iterator

import pytest
from pymongo.errors import ServerSelectionTimeoutError
from pytest_docker.plugin import Services

from moviecenter.movies import (
    Category,
    Movie,
    MovieMongoClient,
    add_movie,
    delete_movie,
    get_all_movies,
    get_movie_by_name,
    get_movie_collection,
)


def is_responsive(client: MovieMongoClient) -> bool:
    try:
        client.admin.command("ping")
        return True
    except ServerSelectionTimeoutError:
        return False


@pytest.fixture(scope="session")
def test_db_connection(  # type: ignore[no-any-unimported]
    docker_ip: str, docker_services: Services
) -> MovieMongoClient:
    port = docker_services.port_for(os.environ["MONGODB_HOSTNAME"], int(os.environ["MONGODB_PORT"]))
    client: MovieMongoClient = MovieMongoClient("mongodb://{}:{}".format(docker_ip, port))
    docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=lambda: is_responsive(client))
    return client


@pytest.fixture
def test_movie_1() -> Movie:
    return Movie(name="LoTR", director="Steve", category=Category.ACTION)


@pytest.fixture
def test_movie_2() -> Movie:
    return Movie(name="Batman v Superman", director="Zack", category=Category.ROMANTIC)


@pytest.fixture
def test_movie_new() -> Movie:
    return Movie(name="Justice League", director="Zack", category=Category.COMEDY)


@pytest.fixture
def test_movies(test_movie_1: Movie, test_movie_2: Movie) -> list[Movie]:
    return [test_movie_1, test_movie_2]


@pytest.fixture(autouse=True)
def populate_db(test_db_connection: MovieMongoClient, test_movies: list[Movie]) -> Iterator[None]:
    movie_collection = get_movie_collection(test_db_connection)
    test_movies_dicts = typing.cast(list[dict[str, typing.Any]], test_movies)
    movie_collection.insert_many(test_movies_dicts)
    yield
    movie_collection.drop()


@pytest.mark.asyncio
async def test_get_all_movies(test_db_connection: MovieMongoClient, test_movies: Movie) -> None:
    assert await get_all_movies(test_db_connection) == test_movies


@pytest.mark.asyncio
async def test_get_movie_by_name_exists(test_db_connection: MovieMongoClient, test_movie_1: Movie) -> None:
    assert await get_movie_by_name(test_db_connection, test_movie_1["name"]) == test_movie_1


@pytest.mark.asyncio
async def test_get_movie_by_name_not_exists(
    test_db_connection: MovieMongoClient,
) -> None:
    assert await get_movie_by_name(test_db_connection, "random") is None


@pytest.mark.asyncio
async def test_add_movie(test_db_connection: MovieMongoClient, test_movie_new: Movie) -> None:
    await add_movie(test_db_connection, test_movie_new)

    m = await get_movie_by_name(test_db_connection, test_movie_new["name"])
    assert m is not None
    del m["_id"]
    assert m == test_movie_new


@pytest.mark.asyncio
async def test_delete_movie(test_db_connection: MovieMongoClient, test_movie_1: Movie) -> None:
    await delete_movie(test_db_connection, test_movie_1["name"])

    assert await get_movie_by_name(test_db_connection, test_movie_1["name"]) is None
