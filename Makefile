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
	tox -q

run:
	uvicorn moviecenter.main:app --reload