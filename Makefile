.DEFAULT_GOAL := default

.PHONY: format lint test run

default:

format:
	isort .
	black .

lint:
	mypy .

test:
	tox -q

run:
	uvicorn moviecenter.main:app --reload