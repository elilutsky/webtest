.DEFAULT_GOAL := default
PYTHON_EXEC := poetry run

.PHONY: format lint test run

default:

format:
	$(PYTHON_EXEC) isort .
	$(PYTHON_EXEC) black .

lint:
	$(PYTHON_EXEC) mypy .
	$(PYTHON_EXEC) flake8 .

test:
	poetry install
	$(PYTHON_EXEC) pytest -vv

run:
	uvicorn moviecenter.main:app --reload