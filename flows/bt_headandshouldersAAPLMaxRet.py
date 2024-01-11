from datetime import datetime
from os import environ

import yfinance as yf
from backtesting import Backtest
from backtesting.lib import TrailingStrategy
from basebot22.basebot import BaseBot
from prefect import flow, task, variables
from tradingpatterns.tradingpatterns import detect_head_shoulder

BOTNAME = "bt_headshoulder_aapl_returnopt"
STOCK = "AAPL"
LOOKBACKYF = "3mo"
LOOKBACK = 76
HOW_MANY_POSITIVE_NEEDED = 2
HOW_MANY_NEGATIVE_NEEDED = 12


def headAndShoulder(df):
    df = detect_head_shoulder(df)
    df["signal"] = 0
    df.loc[df["head_shoulder_pattern"] == "Head and Shoulder", "signal"] = 1
    df.loc[df["head_shoulder_pattern"] == "Inverse Head and Shoulder", "signal"] = -1
    return df["signal"]


class HeadShoulderStrategy(TrailingStrategy):
    hs_lookback = LOOKBACK
    hs_how_many_positive_needed = HOW_MANY_POSITIVE_NEEDED
    hs_how_many_negative_needed = HOW_MANY_NEGATIVE_NEEDED

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
def runBacktest():
    df = yf.download(STOCK, period=LOOKBACKYF, progress=False)
    df = detect_head_shoulder(df)
    bt = Backtest(df, HeadShoulderStrategy, cash=10000, commission=0.002)
    stats = bt.run()
    lastTrade = stats._trades.iloc[-1]
    return lastTrade, df


@task
def actOnDecision(lastTrade, df):
    bot = BaseBot(
        BOTNAME,
        backendurl=environ.get("BACKEND_URL", variables.get("backend_url")),
    )
    portfolio = bot.getPortfolio()
    print("last Trade: ", lastTrade)
    if lastTrade.ExitBar < len(df) - 1 and portfolio.get(STOCK, 0) > 0:
        print("sell!")
        bot.sell(STOCK)
    elif lastTrade.ExitBar == len(df) - 1:
        # trade is still going
        if (
            lastTrade.EntryTime.date() <= datetime.now().date()
            and portfolio.get(STOCK, 0) == 0
        ):
            # buy!!
            print("buy!")
            bot.buy(STOCK, portfolio.get("USD", 0))
    else:
        print("do nothing.")


@flow(log_prints=True)
def btHeadAndShouldersAAPLMaxReturn():
    lastTrade, df = runBacktest()
    actOnDecision(lastTrade, df)
