CRON = "0 20 * * *"  # this doesnt do anything in the script, but is used by the prefect deployment script
from os import environ
from random import randint, random

import numpy as np
import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables


@flow(log_prints=True)
def mainFlow():
    TRADEABLE = [
        "AAPL",
        "MSFT",
        "GOOG",
        "TSLA",
        "AMD",
        "AMZN",
        "DG",
        "KDP",
        "LLY",
        "NOC",
        "NVDA",
        "PGR",
        "UNH",
        "WM",
        "CWEG.L",
        "IWDA.AS",
        "EEM",
        "BTC-USD",
        "ETH-USD",
        "AVAX-USD",
    ]

    bot = BaseBot(
        "randombot",
        backendurl=environ.get("BACKEND_URL", variables.get("backend_url")),
    )
    portfolio = bot.getPortfolio()
    oneSold = False
    for ticker, amount in portfolio.items():
        if ticker == "USD":
            continue
        if random() > 0.9:
            print("selling all " + ticker)
            bot.sell(ticker, -1)
            oneSold = True
    if oneSold:
        portfolio = bot.getPortfolio()
    usd = portfolio["USD"]

    for ticker in TRADEABLE:
        if usd < 10:
            break
        if random() > 0.9:
            print("buying " + ticker)
            if usd < 50:
                amount = usd
            else:
                amount = random() * usd
            print(f"buying {amount}$ of {ticker}")
            bot.buy(ticker, amount)
            usd -= amount
