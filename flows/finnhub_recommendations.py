CRON = "0 16 * * 3"  # this doesnt do anything in the script, but is used by the prefect deployment script
from os import environ

import finnhub
from basebot22.basebot import BaseBot
from prefect import flow, task, variables


@task
def numberRating(rating: dict):
    rate = 0
    rate += rating["strongBuy"] * 2
    rate += rating["buy"] * 1
    rate += rating["sell"] * -1
    rate += rating["strongSell"] * -2
    return rate


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

    finnhub_client = finnhub.Client(api_key=environ["FINNHUB_API_KEY"])

    recs = dict()
    for ticker in TRADEABLE:
        try:
            recs[ticker] = numberRating(finnhub_client.recommendation_trends(ticker)[0])
        except Exception as e:
            print("problem with: ", ticker)
            print(e)

    recs = dict(sorted(recs.items(), key=lambda item: item[1], reverse=True))
    # convert the number to a full rating that equals 1. total
    total = sum(recs.values())
    for key in recs:
        recs[key] = recs[key] / total
    assert sum(recs.values()) == 1

    print("my targets are: ", recs)

    bot = BaseBot(
        f"finnhub-recommendations",
        backendurl=variables.get("backend_url"),
    )
    portfolio = bot.getPortfolio()
    usd = portfolio["USD"]

    # first check sells
    for ticker, target in recs.items():
        if ticker in portfolio and target < 0:
            print("selling ", ticker)
            bot.sell(ticker, -1)

    portfolio = bot.getPortfolio()
    usd = portfolio["USD"]
    # then check buys
    for ticker, target in recs.items():
        try:
            if ticker not in portfolio and target > 0:
                print("buying ", ticker)
                bot.buy(ticker, usd * target, amountInUSD=True)
            elif ticker in portfolio and target > 0:
                diff = (target * usd) - (
                    portfolio[ticker] * bot.getCurrentPrice(ticker)
                )
                if diff > 0:
                    print("rebalancing buy ", ticker)
                    bot.buy(ticker, diff, amountInUSD=True)
        except Exception as e:
            print("problem with: ", ticker, ". skip")
            print(e)
