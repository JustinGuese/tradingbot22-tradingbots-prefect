from datetime import datetime, timedelta
from os import environ

import pandas as pd
import psycopg2
from basebot22.basebot import BaseBot
from prefect import flow, task, variables


# PSQL_URL
@task
def getCurrentNewsWinners():
    URI = environ["PSQL_URL"]
    user = URI.split(":")[0]
    password = URI.split(":")[1].split("@")[0]
    host = URI.split("@")[1].split(":")[0]
    port = URI.split(":")[2].split("/")[0]
    database = URI.split("/")[1]
    db = psycopg2.connect(
        dsn=f"host={host} port={port} dbname={database} user={user} password={password}"
    )
    cur = db.cursor()

    startstamp = datetime.utcnow() - timedelta(days=1)
    sql = f"select ticker, timestamp, article_relevance_score, article_sentiment_score from public.alphavantage_sentiment where timestamp > '{startstamp}' and article_relevance_score > 0.8 order by timestamp desc"
    cur.execute(sql)
    rows = cur.fetchall()
    df = pd.DataFrame(
        rows,
        columns=[
            "ticker",
            "timestamp",
            "article_relevance_score",
            "article_sentiment_score",
        ],
    )

    # order by article_sentiment_score desc
    df = df.sort_values(by=["article_sentiment_score"], ascending=False)
    return df


@task
def investOnInfo(df, bot, portfolio):
    # only keep first entry of each
    negatives = df[df.article_sentiment_score < -0.3]
    soldOne = False
    for neg in negatives.ticker.unique():
        if neg in portfolio:
            # we have to sell everything
            print(
                "negative news for a stock in our portfolio, sell all. ticker: " + neg
            )
            bot.sell(neg)
            soldOne = True
    if soldOne:
        # refresh
        portfolio = bot.getPortfolio()
    cash = portfolio["USD"]
    # only keep those with sentiment_score bigger .7
    df = df[df.article_sentiment_score > 0.65]
    # deduplicate, keep first
    df = df.drop_duplicates(subset=["ticker"], keep="first")
    if len(df) > 0:
        if len(df) <= 2:
            # only invest half max if less than two stocks
            cash /= 2
        for index, row in df.iterrows():
            print("investing in: " + row["ticker"])
            bot.buy(row["ticker"], cash / len(df))


@flow(log_prints=True)
def newsTrader():
    print("starting")
    bot = BaseBot(
        "newstrader",
        backendurl=environ.get("BACKEND_URL", variables.get("backend_url")),
    )
    portfolio = bot.getPortfolio()
    df = getCurrentNewsWinners()
    investOnInfo(df, bot, portfolio)


if __name__ == "__main__":
    newsTrader()
