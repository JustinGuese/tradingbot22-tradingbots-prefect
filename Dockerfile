FROM python:3.11-slim
RUN apt update && apt install postgresql-client -y
RUN pip install poetry prefect
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi --no-root
COPY ./flows/ /app/flows/
CMD ["prefect", "worker", "start", "--pool", "docker-tradingbot-worker"]