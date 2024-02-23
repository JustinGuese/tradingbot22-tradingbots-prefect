CRON = "30 17 1,5,9,13,17,21,25,29 * *"
# jupyternotebooks/trenddetection.ipynb
# tuned parameters according to QQQ index: {'steps': 4, 'predlookback': 7}
import pickle
import warnings
from os import environ

import numpy as np
import pandas as pd
import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, get_run_logger, task, variables
from ta import add_all_ta_features
from trendet import identify_df_trends

warnings.filterwarnings("ignore")

COLORDER = [
    "Adj Close",
    "Close",
    "High",
    "Low",
    "Open",
    "Volume",
    "volume_adi",
    "volume_obv",
    "volume_cmf",
    "volume_fi",
    "volume_em",
    "volume_sma_em",
    "volume_vpt",
    "volume_vwap",
    "volume_mfi",
    "volume_nvi",
    "volatility_bbm",
    "volatility_bbh",
    "volatility_bbl",
    "volatility_bbw",
    "volatility_bbp",
    "volatility_bbhi",
    "volatility_bbli",
    "volatility_kcc",
    "volatility_kch",
    "volatility_kcl",
    "volatility_kcw",
    "volatility_kcp",
    "volatility_kchi",
    "volatility_kcli",
    "volatility_dcl",
    "volatility_dch",
    "volatility_dcm",
    "volatility_dcw",
    "volatility_dcp",
    "volatility_atr",
    "volatility_ui",
    "trend_macd",
    "trend_macd_signal",
    "trend_macd_diff",
    "trend_sma_fast",
    "trend_sma_slow",
    "trend_ema_fast",
    "trend_ema_slow",
    "trend_vortex_ind_pos",
    "trend_vortex_ind_neg",
    "trend_vortex_ind_diff",
    "trend_trix",
    "trend_mass_index",
    "trend_dpo",
    "trend_kst",
    "trend_kst_sig",
    "trend_kst_diff",
    "trend_ichimoku_conv",
    "trend_ichimoku_base",
    "trend_ichimoku_a",
    "trend_ichimoku_b",
    "trend_stc",
    "trend_adx",
    "trend_adx_pos",
    "trend_adx_neg",
    "trend_cci",
    "trend_visual_ichimoku_a",
    "trend_visual_ichimoku_b",
    "trend_aroon_up",
    "trend_aroon_down",
    "trend_aroon_ind",
    "trend_psar_up",
    "trend_psar_down",
    "trend_psar_up_indicator",
    "trend_psar_down_indicator",
    "momentum_rsi",
    "momentum_stoch_rsi",
    "momentum_stoch_rsi_k",
    "momentum_stoch_rsi_d",
    "momentum_tsi",
    "momentum_uo",
    "momentum_stoch",
    "momentum_stoch_signal",
    "momentum_wr",
    "momentum_ao",
    "momentum_roc",
    "momentum_ppo",
    "momentum_ppo_signal",
    "momentum_ppo_hist",
    "momentum_pvo",
    "momentum_pvo_signal",
    "momentum_pvo_hist",
    "momentum_kama",
    "others_dr",
    "others_dlr",
    "others_cr",
    "Signal",
]


def labelToSignal(df):
    signal = []
    crntSig = 0
    if "Up Trend" not in df.columns or "Down Trend" not in df.columns:
        if "Up Trend" not in df.columns:
            df["Up Trend"] = "n"
        if "Down Trend" not in df.columns:
            df["Down Trend"] = "n"
    elif "Up Trend" not in df.columns and "Down Trend" not in df.columns:
        raise ValueError("Up Trend and Down Trend not in columns")
    for i in range(len(df)):

        if df["Up Trend"][i] == "n" and df["Down Trend"][i] == "n":
            # look into future, which is the one label that is not "n"
            nextSig = None
            for j in range(i, len(df)):
                if df["Up Trend"][j] != "n" or df["Down Trend"][j] != "n":
                    if df["Close"][j] > df["Close"][i]:
                        nextSig = 1
                    else:
                        nextSig = -1
                    break
            if nextSig is None:
                # print("next sig is none at ", i, j)
                nextSig = 0
            else:
                crntSig = nextSig
        if df["Up Trend"][i] != "n":
            crntSig = 1
        elif df["Down Trend"][i] != "n":
            crntSig = -1
        signal.append(crntSig)
    return signal


@flow(log_prints=True)
def mainFlow():
    PREDLOOKBACK = 7

    BOTNAME = "xgb_sharpeopt_trenddet"

    bot = BaseBot(
        BOTNAME,
        backendurl=environ.get("BACKEND_URL", variables.get("backend_url")),
    )

    tickerSelection = pd.read_csv("../xgboost-trend-sharpeopt/toInvest.csv")
    tickerSelection = tickerSelection.set_index("ticker")
    print(tickerSelection)

    portfolio = bot.getPortfolio()
    print("crnt portfolio: ", portfolio)

    trades = dict()
    for ticker, weight in tickerSelection.iterrows():
        with open(f"../xgboost-trend-sharpeopt/{ticker}.model", "rb") as f:
            model = pickle.load(f)
        df = yf.download(
            ticker,
            period="3mo",
            progress=False,
        )
        df = add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume")
        df = identify_df_trends(df, "Close")
        df["Signal"] = labelToSignal(df)
        df = df.drop(["Up Trend", "Down Trend"], axis=1)
        df = df[COLORDER]

        pred = model.predict(df)
        crntPred = np.median(pred[-PREDLOOKBACK:])
        print(f"Prediction for {ticker}: {crntPred}")

        stock = portfolio.get(ticker, 0)
        if crntPred == 1.0:
            trades[ticker] = 1
        elif crntPred == 0.0 and stock > 0:
            trades[ticker] = -1

    # first execute the sales
    if len(trades) > 0:
        for ticker, trade in trades.items():
            if trade == -1:
                print("selling all of ", ticker)
                bot.sell(ticker)
        # get crnt cash
        portfolio = bot.getPortfolio()
        cash = portfolio.get("USD", 0)
        if cash < 10:
            raise ValueError("not enough cash to buy: " + str(portfolio))
        # then execute the buys
        toBuy = dict()
        for ticker, trade in trades.items():
            if trade == 1:
                toBuy[ticker] = tickerSelection["weight"][ticker]
        toBuy = pd.Series(toBuy)
        toBuy = toBuy / toBuy.sum()
        for ticker, weight in toBuy.items():
            amount = cash * weight
            print(f"buying {round(amount,2)}$ of {ticker}")
            bot.buy(ticker, amount, amountInUSD=True)
    else:
        print("crntly no trades...")
    print("fin.")


if __name__ == "__main__":
    mainFlow()
