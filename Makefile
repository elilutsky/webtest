.PHONY: lint test run

lint:
	mypy .

test:
	tox -q

run:
	uvicorn moviecenter.main:app --reload