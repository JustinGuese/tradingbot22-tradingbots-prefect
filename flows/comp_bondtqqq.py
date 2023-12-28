from datetime import datetime, timedelta
from os import environ

import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables

# from platform import node, platform


@task
def calculateCumRet(stocks: list, days: int = 20):
    print(f"calculating cumulative return for {stocks}")
    cumret = dict()
    for ticker in stocks:
        df = yf.download(ticker, start=datetime.now() - timedelta(days=days * 2))
        # calculate the cumulative return 20d
        df["20d_cumulative_return"] = (df["Close"] / df["Close"].shift(days)) - 1
        cumret[ticker] = df["20d_cumulative_return"].iloc[-1]
    return cumret


@flow(log_prints=True)
def compBondTQQQ():
    bot = BaseBot(
        "composer-bondtqqq-v1",
        backendurl=environ["BACKEND_URL"],
    )
    # calculate cumret
    cum60 = calculateCumRet(["BND", "BIL"], 60)

    # if 60d cumret of BND is greater than BIL
    toBuy = []
    if cum60["BND"] >= cum60["BIL"]:
        # rates are not going up
        # calculate 10d max drawdown of QQQ
        # Download QQQ data for the last 20 days
        qqq = yf.download("QQQ", start=datetime.now() - timedelta(days=10))
        # Calculate the daily drawdowns
        qqq["drawdown"] = 1 - (qqq["Close"] / qqq["Close"].cummax())
        # Find the max drawdown
        max_drawdown = qqq["drawdown"].max()
        if max_drawdown > 0.05:
            # if greater than 5 pxt
            # QQQ was down recently
            # if 5 day cumret of SVXY is less or equal 0
            cum5 = calculateCumRet(["SVXY"], 5)
            if cum5["SVXY"] <= 0:
                # high volume , go safe
                # all in TMF treasury bull
                print("high volume, all in TMF")
                toBuy = ["TMF"]
            else:
                # low volume, all in TQQQ
                print("low volume, all in TQQQ")
                toBuy = ["TQQQ"]
        else:
            # QQQ was not down recently
            # all in TQQQ
            print("all in TQQQ, bc qqq was not down")
            toBuy = ["TQQQ"]
    else:
        # rates are going up
        cum2 = calculateCumRet(["BND"], 2)
        if cum2["BND"] >= 0:
            # 50/50 between QQQ and safe bonds
            print("50/50 between QQQ and safe bonds")
            toBuy = ["QQQ", "BND"]
        else:
            # full safety mode, all bonds
            print("full safety mode, all bonds")
            toBuy = ["BND", "GLD"]

    portfolio = bot.getPortfolio()
    needRebalance = False
    for tick in toBuy:
        if tick not in list(portfolio.keys()):
            needRebalance = True
            break
    if needRebalance:
        # sell all
        for ticker, amount in portfolio.items():
            if ticker != "USD":
                print("selling all shares of ", ticker)
                bot.sell(ticker)
        portfolio = bot.getPortfolio()
        cash = portfolio["USD"]
        cashPerStock = cash / len(toBuy)
        for ticker in toBuy:
            print("buying ", ticker, " for ", cashPerStock, " USD")
            bot.buy(ticker, amount=cashPerStock)
    else:
        print("no rebalance requried. portoflio: ", portfolio)


# schedule=(CronSchedule(cron="15 22 * * *", timezone="Europe/Berlin")),
