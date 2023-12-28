FROM prefecthq/prefect:2-python3.11
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
COPY ./flows/ /app/
# deploy all flows
RUN python addAllFlows.py
CMD ["prefect", "worker", "start", "--pool", "caprover-docker-container" ]