CRON = "6 17 * * *"  # this doesnt do anything in the script, but is used by the prefect deployment script
import json
import logging
from datetime import datetime
from os import environ

import yfinance as yf
from backtesting import Backtest
from backtesting.lib import TrailingStrategy
from basebot22.basebot import BaseBot
from prefect import flow, get_run_logger, task, variables
from tqdm import tqdm
from tradingpatterns.tradingpatterns import detect_head_shoulder

# based on backtest/backtest_headAndShoulders-Sharpeopt.ipynb
with open("./flows/backtest_headshoulder_sharpemix_results.json", "r") as f:
    RESULTS = json.load(f)

BOTNAME = "bt_headshoulder_sharpeopt_mixed"
# STOCK = "AAPL"
# LOOKBACKYF = "3mo"
# LOOKBACK = 76
# HOW_MANY_POSITIVE_NEEDED = 2
# HOW_MANY_NEGATIVE_NEEDED = 12


def headAndShoulder(df):
    df = detect_head_shoulder(df)
    df["signal"] = 0
    df.loc[df["head_shoulder_pattern"] == "Head and Shoulder", "signal"] = 1
    df.loc[df["head_shoulder_pattern"] == "Inverse Head and Shoulder", "signal"] = -1
    return df["signal"]


class HeadShoulderStrategy(TrailingStrategy):
    hs_lookback = None
    hs_how_many_positive_needed = None
    hs_how_many_negative_needed = None

    def init(self):
        self.hs_signal = self.I(headAndShoulder, self.data.df)

    def next(self):
        lookback = (
            self.hs_lookback if len(self.data) >= self.hs_lookback else len(self.data)
        )
        howManyBuySignals = sum(self.hs_signal[-lookback:] == 1)
        howManySellSignals = sum(self.hs_signal[-lookback:] == -1)

        if (
            howManyBuySignals >= self.hs_how_many_positive_needed
            and self.position.size == 0
        ):
            self.buy()
        elif (
            howManySellSignals >= self.hs_how_many_negative_needed
            and self.position.size > 0
        ):
            self.position.close()


@task
def runBacktest(
    stock, lookback, howManyPositive, howManyNegative, logger, LOOKBACKYF="3mo"
):
    df = yf.download(stock, period=LOOKBACKYF, progress=False)
    df = detect_head_shoulder(df)
    bt = Backtest(df, HeadShoulderStrategy, cash=10000, commission=0.002)
    stats = bt.run(
        hs_lookback=lookback,
        hs_how_many_positive_needed=howManyPositive,
        hs_how_many_negative_needed=howManyNegative,
    )
    try:
        lastTrade = stats._trades.iloc[-1]
    except Exception as e:
        # no trade, increase yflookback
        if LOOKBACKYF == "1y":
            raise Exception("no trade in 1y retry: " + str(e))
        logger.warning(
            "could not get a trade in the last 3 months, increasing yf lookback to 1y"
        )
        # no recursion allowed
        df = yf.download(stock, period="1y", progress=False)
        df = detect_head_shoulder(df)
        bt = Backtest(df, HeadShoulderStrategy, cash=10000, commission=0.002)
        stats = bt.run(
            hs_lookback=lookback,
            hs_how_many_positive_needed=howManyPositive,
            hs_how_many_negative_needed=howManyNegative,
        )
        lastTrade = stats._trades.iloc[-1]
    return lastTrade, df


@task
def actOnDecision(stock, usdamount, lastTrade, df, bot, portfolio):
    print("last Trade: ", stock, lastTrade)
    if lastTrade.ExitBar < len(df) - 1 and portfolio.get(stock, 0) > 0:
        print(f"selling all {stock} bc trade signal is over.")
        bot.sell(stock)
    elif lastTrade.ExitBar == len(df) - 1:
        # trade is still going
        if (
            lastTrade.EntryTime.date() <= datetime.now().date()
            and portfolio.get(stock, 0) == 0
        ):
            # buy!!
            print(f"buying {stock} for {usdamount}")
            bot.buy(stock, usdamount)
    else:
        print("do nothing.")


@flow(log_prints=True)
def mainFlow():
    logger = get_run_logger()
    bot = BaseBot(
        BOTNAME,
        backendurl=environ.get("BACKEND_URL", variables.get("backend_url")),
    )
    portfolio = bot.getPortfolio()
    # first sell everything that is not part of RESULTS anymore
    for ticker in portfolio.keys():
        if ticker == "USD":
            continue
        if ticker not in RESULTS.keys():
            logger.info("selling ticker bc not in results anymore: ", ticker)
            bot.sell(ticker)
    portfolio = bot.getPortfolio()
    cash = portfolio["USD"]
    for ticker, stats in tqdm(RESULTS.items()):
        try:
            cashForStock = stats["weight"] * cash
            if cashForStock < 50:
                logger.warning(
                    f"not enough cash for {ticker}, skipping. would have assigned: {cashForStock}"
                )
                continue
            if stats["hs_lookback"] > 80:
                yflookback = "1y"
            else:
                yflookback = "3mo"
            lastTrade, df = runBacktest(
                ticker,
                stats["hs_lookback"],
                stats["hs_how_many_positive_needed"],
                stats["hs_how_many_negative_needed"],
                logger,
                yflookback,
            )
            actOnDecision(ticker, cashForStock, lastTrade, df, bot, portfolio)
        except Exception as e:
            logger.error(
                f"error in {ticker}. with settings {stats} and yflookback {yflookback} skip: {e}"
            )
    lastTrade, df = runBacktest(
        ticker,
        stats["hs_lookback"],
        stats["hs_how_many_positive_needed"],
        stats["hs_how_many_negative_needed"],
        logger,
        yflookback,
    )
    actOnDecision(lastTrade, df)


if __name__ == "__main__":
    mainFlow.run()
