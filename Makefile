.DEFAULT_GOAL := default

.PHONY: format lint test run

default:

format:
	poetry run isort .
	poetry run black .

lint:
	poetry run mypy .
	poetry run flake8 .

test:
	poetry install
	poetry run pytest -vv

run:
	uvicorn moviecenter.main:app --reload