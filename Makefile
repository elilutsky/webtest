.DEFAULT_GOAL := default

.PHONY: format lint test run

default:

format:
	isort .
	black .

lint:
	mypy .
	flake8 .

test:
	poetry install
	poetry run pytest -vv

run:
	uvicorn moviecenter.main:app --reload