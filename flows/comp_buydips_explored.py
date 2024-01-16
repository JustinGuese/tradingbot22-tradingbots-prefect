CRON = "30 1 * * *"  # this doesnt do anything in the script, but is used by the prefect deployment script
from datetime import datetime, timedelta
from os import environ

import yfinance as yf

# further adapted, see notebook jupyternotebooks/composer-buythedrip.ipynb
from basebot22.basebot import BaseBot
from prefect import flow, task, variables


@task
def switchPair(tickerWanted, bot):
    portfolio = bot.getPortfolio()
    if tickerWanted == "TQQQ":
        TOSELL = "SQQQ"
        TOBUY = "TQQQ"
    elif tickerWanted == "SQQQ":
        TOSELL = "TQQQ"
        TOBUY = "SQQQ"
    else:
        raise ValueError("tickerWanted must be either TQQQ or sqqq")
    tosell = portfolio.get(TOSELL, 0)
    if tosell > 0:
        print("selling all ", TOSELL)
        bot.sell(TOSELL)
        portfolio = bot.getPortfolio()  # refresh
    usd = portfolio.get("USD", 0)
    if usd > 50:
        print("buying %s with USD: " % TOBUY, usd)
        bot.buy(TOBUY, amount=usd, amountInUSD=True)
    else:
        print("not enough cash or already holding %s" % TOBUY)


@flow(log_prints=True)
def mainFlow():
    bot = BaseBot(
        "composer-buydipsqqq-shorting-explored",
        backendurl=variables.get("backend_url"),
    )
    qqq = yf.download("QQQ", start=datetime.now() - timedelta(days=100))

    # explored in notebook: use cum sum return with lookback 1, and threshold
    lookback = 1
    threshold = 0.7842105263157895

    qqq["cumulative_5d_return"] = qqq["Adj Close"].pct_change(lookback).cumsum()
    crntThreshold = qqq["cumulative_5d_return"].iloc[-1]

    if crntThreshold > threshold:
        # buy tqqq
        switchPair("TQQQ", bot)
    else:
        # buy sqqq
        switchPair("SQQQ", bot)
