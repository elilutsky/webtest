from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from pymongo.collection import Collection
from typing_extensions import NotRequired, TypedDict


class Movie(TypedDict):
    _id: NotRequired[ObjectId]
    name: str
    director: str
    budget: int


MovieMongoClient = MongoClient[Movie]


def get_movie_collection(db_connection: MovieMongoClient) -> Collection[Movie]:
    database = db_connection.movies
    return database.movies


async def get_all_movies(db_connection: MovieMongoClient) -> list[Movie]:
    movie_collection = get_movie_collection(db_connection)
    return list(movie_collection.find({}))


async def get_movie_by_name(db_connection: MovieMongoClient, name: str) -> Movie | None:
    movie_collection = get_movie_collection(db_connection)
    if (movie := movie_collection.find_one({"name": name})) is not None:
        return movie
    else:
        return None


async def add_movie(db_connection: MovieMongoClient, movie: Movie) -> None:
    movie_collection = get_movie_collection(db_connection)
    movie_collection.insert_one(jsonable_encoder(movie))


async def delete_movie(db_connection: MovieMongoClient, name: str) -> None:
    movie_collection = get_movie_collection(db_connection)
    movie_collection.delete_one({"name": name})
