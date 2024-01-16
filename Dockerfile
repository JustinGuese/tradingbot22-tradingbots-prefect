FROM prefecthq/prefect:2-python3.11
RUN apt update && apt install postgresql-client hugo -y
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi --no-root
CMD ["prefect", "agent", "start", "--pool", "docker-caprover-container-sb"]
# remember that this one needs docker socket access!