FROM python:3.10-slim AS builder

WORKDIR /app

RUN pip install poetry==1.2.1 && poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --without=dev --no-ansi
RUN poetry install --only-root --no-ansi

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /app /app
ADD . /app

EXPOSE 8000

CMD .venv/bin/python -m uvicorn moviecenter.main:app --host 0.0.0.0 --port 8000