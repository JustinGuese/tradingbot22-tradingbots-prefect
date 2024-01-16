CRON = "20 1 * * *"  # this doesnt do anything in the script, but is used by the prefect deployment script
from datetime import datetime, timedelta
from os import environ
from pathlib import Path

import pandas as pd
import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables

logger = None


@task
def basicSetup():
    global logger
    bot = BaseBot(
        "composer-boring-v1",
        backendurl=variables.get("backend_url"),
    )
    # create folder persistent if not exists
    Path("persistent").mkdir(parents=True, exist_ok=True)
    # check if notBoringCurrentMode.txt exists, if not create it
    if not Path("./persistent/notBoringnotBoringCurrentMode.txt").is_file():
        print(
            "notBoringCurrentMode.txt not found, creating it. this should only happen the first execution of the flow!"
        )
        Path("./persistent/notBoringCurrentMode.txt").touch()
    with open("./persistent/notBoringCurrentMode.txt", "r") as f:
        currentMode = f.read()
        if currentMode == "":
            currentMode = "none"
    return bot, currentMode


# helper functions
@task
def switchMode(mode):
    with open("./persistent/notBoringCurrentMode.txt", "w+") as f:
        f.write(mode)
    return mode


@task
def get10DayMaxDrawdown(ticker, bot):
    qqq = yf.download(ticker, start=datetime.now() - timedelta(days=100))
    rollMax = qqq["Adj Close"].rolling(10, min_periods=1).max()
    dailyDrawdown = qqq["Adj Close"] / rollMax - 1.0
    maxDailyDrawdown = dailyDrawdown.rolling(10, min_periods=1).min()
    crntMaxDailyDrawdown = maxDailyDrawdown[-1]
    return crntMaxDailyDrawdown


def calculateCurrent45dVolatility(df):
    df["daily_returns"] = df["Adj Close"].pct_change()
    df["daily_volatility"] = df["daily_returns"].rolling(45).std()
    return df["daily_volatility"][-1]


@task
def inverseVolatilityWeights(tickers, bot):
    crntVolatilities = dict()
    for ticker in tickers:
        df = yf.download(ticker, start=datetime.now() - timedelta(days=100))
        crntVolatilities[ticker] = calculateCurrent45dVolatility(df)
    for ticker, volatility in crntVolatilities.items():
        crntVolatilities[ticker] = 1 / volatility
    weights = dict()
    for ticker, volatility in crntVolatilities.items():
        weights[ticker] = crntVolatilities[ticker] / sum(crntVolatilities.values())
    return weights


@task
def buyAccordingToWeights(weights, bot):
    global logger
    portfolio = bot.getPortfolio()
    usd = portfolio["USD"]
    if len(portfolio) > 1:
        for ticker, amount in portfolio.items():
            if ticker != "USD":
                bot.sell(ticker)
        portfolio = bot.getPortfolio()
        usd = portfolio["USD"]
        # buy according to weights
        if usd > 50:
            for ticker, weight in weights.items():
                print(f"buying {weight*usd}$ of {ticker}")
                bot.buy(ticker, amount=weight * usd, amountInUSD=True)
        else:
            print("not enough usd to buy u poor f#k")


@flow(log_prints=True)
def mainFlow():
    bot, currentMode = basicSetup()
    #### trade logic
    qqqCrntMaxDailyDrawdown = get10DayMaxDrawdown("QQQ", bot)
    if qqqCrntMaxDailyDrawdown < -0.06:  # question: how is the "grater than" meant?
        print("risk off mode")
        if currentMode != "risk off":
            currentMode = switchMode("risk off")
            print("switching mode to risk off")
            # get 45d inverse volatility weights
            weights = inverseVolatilityWeights(
                ["GLD", "TMF", "FAS", "TQQQ", "UUP"], bot
            )
            print(weights)
            buyAccordingToWeights(weights, bot)
    else:
        # if 10d max drawdown of TMF is greather than 7%
        # "risk off mode"
        tmfCrntMaxDailyDrawdown = get10DayMaxDrawdown("TMF", bot)
        if tmfCrntMaxDailyDrawdown < -0.07:
            print("risk off mode")
            if currentMode != "risk off":
                currentMode = switchMode("risk off")
                print("switching mode to risk off")
                # get 45d inverse volatility weights
                weights = inverseVolatilityWeights(
                    ["GLD", "TMF", "FAS", "TQQQ", "UUP"], bot
                )
                # print("current weights " + weights)
                buyAccordingToWeights(weights, bot)
        else:
            # "risk on mode"
            # inverse volatility weight 45d = Assets that are more volatile receive lower weights
            # TMF, FAS, TQQQ (treasury bull 3x, financial bull 3x, 3x qqq)
            print("risk off on")
            if currentMode != "risk on":
                currentMode = switchMode("risk on")
                print("switching mode to risk on")
                # get 45d inverse volatility weights
                weights = inverseVolatilityWeights(["TMF", "FAS", "TQQQ"], bot)
                # print("current target weights " + weights)
                buyAccordingToWeights(weights, bot)
    portfolio = bot.getPortfolio()
    print(portfolio)
