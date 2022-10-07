FROM python:3.10-slim AS builder

RUN pip install poetry==1.2.1

COPY pyproject.toml poetry.lock ./
RUN poetry export -o requirements.txt

FROM python:3.10-slim

WORKDIR /app

RUN groupadd -r umovie && useradd --no-log-init -r -g umovie umovie

COPY --from=builder requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8000

USER umovie

CMD uvicorn moviecenter.main:app --host 0.0.0.0 --port 8000