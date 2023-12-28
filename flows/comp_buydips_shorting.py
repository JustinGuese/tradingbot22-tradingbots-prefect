# see: tradingbot22-tradingbots/jupyternotebooks/composer.ipynb
from datetime import datetime, timedelta
from os import environ

import yfinance as yf

# adapted to not use sqqq, but SQQQ, shorting the QQQ
from basebot22.basebot import BaseBot
from prefect import flow, task, variables


@task
def switchPair(bot, tickerWanted):
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
def buydipsShorting():
    # basic setup
    bot = BaseBot(
        "composer-buydipsqqq-shorting",
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
            # buy sqqq, why?
            switchPair(bot, "SQQQ")
        else:
            # buy tqqq
            switchPair(bot, "TQQQ")
    else:
        # sell all tqqq, buy sqqq
        switchPair(bot, "SQQQ")
