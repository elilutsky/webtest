import os

from fastapi import FastAPI

from moviecenter.app import movies_router
from moviecenter.movies import MovieMongoClient


def get_mongodb_connection() -> MovieMongoClient:
    return MovieMongoClient(
        f"mongodb://{os.environ['MONGODB_HOSTNAME']}:{os.environ['MONGODB_PORT']}"
    )


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(movies_router)
    app.state.db = get_mongodb_connection()

    return app


app = create_app()
