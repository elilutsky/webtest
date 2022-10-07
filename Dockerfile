FROM python:3.10-slim AS builder

RUN pip install poetry==1.2.1 && poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./
RUN poetry export -o requirements.txt

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8000

CMD uvicorn moviecenter.main:app --host 0.0.0.0 --port 8000