.PHONY: format lint test run

format:
	isort .
	black .

lint:
	mypy .

test:
	tox -q

run:
	uvicorn moviecenter.main:app --reload