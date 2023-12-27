FROM prefecthq/prefect:2-python3.11
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
COPY ./flows/ /app/
CMD ["prefect", "worker", "start", "--pool", "caprover-prefect-docker-worker" ]