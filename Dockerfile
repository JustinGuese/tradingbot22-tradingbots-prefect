FROM prefecthq/prefect:2-python3.11
RUN apt update && apt install postgresql-client hugo -y
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi --no-root
COPY ./flows/ /app/flows/
COPY tradingbot-website-generator/ /app/flows/tradingbot-website-generator/ 
WORKDIR /app/flows/
CMD ["./deployAndRun.sh" ]