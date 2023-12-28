# see: tradingbot22-tradingbots/jupyternotebooks/composer.ipynb
from datetime import datetime, timedelta
from os import environ

import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables


@task
def switchPair(bot, tickerWanted):
    portfolio = bot.getPortfolio()
    if tickerWanted == "TQQQ":
        TOSELL = "BSV"
        TOBUY = "TQQQ"
    elif tickerWanted == "BSV":
        TOSELL = "TQQQ"
        TOBUY = "BSV"
    else:
        raise ValueError("tickerWanted must be either TQQQ or BSV")
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
def buydipsOriginal():
    # basic setup
    bot = BaseBot(
        "composer-buydipsqqq-original",
        backendurl=variables.get("backend_url"),
    )

    # calculate 5 day cumulative return of qqq
    qqq = yf.download("QQQ", start=datetime.now() - timedelta(days=15))
    # 5 day cumulative return of qqq
    qqq["cumulative_return"] = qqq["Adj Close"].pct_change(5).cumsum()
    qqqCrnt5DCumRet = qqq["cumulative_return"][-1]
    print("qqq now: ", qqqCrnt5DCumRet)
    if qqqCrnt5DCumRet < -0.05:  # if less than -5%
        # if 1d cumret of tqqq greater than 5%
        tqqq = yf.download("TQQQ", start=datetime.now() - timedelta(days=5))
        tqqq["cumulative_return"] = tqqq["Adj Close"].pct_change(1).cumsum()
        tqqqCrnt5DCumRet = tqqq["cumulative_return"][-1]
        print("tqqq now: ", tqqqCrnt5DCumRet)
        if tqqqCrnt5DCumRet > 0.05:
            # buy bsv, why?
            switchPair(bot, "BSV")
        else:
            # buy tqqq
            switchPair(bot, "TQQQ")
    else:
        # sell all tqqq, buy bsv
        switchPair(bot, "BSV")
