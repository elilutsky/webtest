.DEFAULT_GOAL := default
PYTHON_EXEC := poetry run
IMAGE := moviecenter
VERSION := 0.1.0
ENV := .env.dev

.PHONY: format lint test run

default:

format:
	$(PYTHON_EXEC) isort .
	$(PYTHON_EXEC) black .

lint:
	$(PYTHON_EXEC) mypy .
	$(PYTHON_EXEC) flake8 .

test:
	$(PYTHON_EXEC) pytest -vv

check: format lint test

build:
	docker build -t $(IMAGE):$(VERSION) -t $(IMAGE):latest .

run:
	docker compose --env-file $(ENV) -f docker-compose.yaml -f docker-compose.dev.yaml up -d