# jupyternotebooks/trend-shapreopt.ipynb
from os import environ

import pandas as pd
import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables
from ta.volatility import BollingerBands


@task
def pairTrade(TICKER1, TICKER2, WINDOW=20, Z=0.5, MIDDLE_Z=0.1):
    # ('GLRI', 'VSTM', 20, 0.5, 0.1)
    BOTNAME = "pairTrade-" + TICKER1 + "-" + TICKER2

    bot = BaseBot(BOTNAME, backendurl=variables.get("backend_url"))

    df = yf.download([TICKER1, TICKER2], period="2mo", progress=False)["Close"]
    df = df.fillna(method="ffill")
    df = df.fillna(method="bfill")
    # df.head()

    spread = pd.DataFrame()
    spread["spread"] = df[TICKER1] - df[TICKER2] * (df[TICKER1][0] / df[TICKER2][0])
    indicator_bb = BollingerBands(close=spread["spread"], window=WINDOW, window_dev=Z)
    spread["bb_m"] = indicator_bb.bollinger_mavg()
    spread["bb_h"] = indicator_bb.bollinger_hband()
    spread["bb_l"] = indicator_bb.bollinger_lband()

    portfolio = bot.getPortfolio()

    i = len(spread) - 1
    if spread.iloc[i]["spread"] > spread.iloc[i]["bb_h"] and portfolio["USD"] > 0:
        # crossing the top bollinger band
        # short pair, short first, long second
        # first sell crnt Shit
        if portfolio.get(TICKER1, 0) == 0 and portfolio.get(TICKER2, 0) == 0:
            # short first, long second
            buyFor = portfolio["USD"] / 2
            bot.buy(TICKER1, amount=buyFor, amountInUSD=True, short=True)
            # long JRVR
            bot.buy(TICKER2, amount=buyFor, amountInUSD=True)

            portfolio = bot.getPortfolio()

            print(f"entering Short Pair at {i}, crnt portfolio {portfolio}")
    elif (
        spread.iloc[i]["spread"] > spread.iloc[i]["bb_m"] * MIDDLE_Z
        and spread.iloc[i - 1]["spread"] <= spread.iloc[i - 1]["bb_m"] * MIDDLE_Z
    ) or (
        spread.iloc[i]["spread"] < spread.iloc[i]["bb_m"] * (1 - MIDDLE_Z)
        and spread.iloc[i - 1]["spread"] >= spread.iloc[i - 1]["bb_m"] * (1 - MIDDLE_Z)
    ):
        # if we had a cross middle line of spread event
        if portfolio.get(TICKER1, 0) != 0:
            # ... and we are currently in a trade, liquidate it
            bot.sell(TICKER1, amount=-1, short=portfolio.get(TICKER1) < 0)
            bot.sell(TICKER2, amount=-1, short=portfolio.get(TICKER2) < 0)

            portfolio = bot.getPortfolio()
            print(f"liquidate at {i}, crnt portfolio {portfolio}")
    elif spread.iloc[i]["spread"] < spread.iloc[i]["bb_l"] and portfolio["USD"] > 0:
        if portfolio.get(TICKER1, 0) == 0 and portfolio.get(TICKER2, 0) == 0:
            # crossing the bottom bollinger band
            # long pair, long first, short second
            # long FUTU
            buyFor = portfolio["USD"] / 2

            bot.buy(TICKER1, amount=buyFor, amountInUSD=True)
            # short second
            bot.buy(TICKER2, amount=buyFor, amountInUSD=True, short=True)

            portfolio = bot.getPortfolio()
            print(f"long pair {i}, crnt portfolio {portfolio}")
