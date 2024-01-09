from os import environ

import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables
from ta.momentum import PercentageVolumeOscillator

# for the why check jupyternotebooks/predict_blackberry_fall.ipynb


@flow(log_prints=True)
def momentumPVOSignalMSFT():
    print("connecting to backend...")
    bot = BaseBot(
        "momentum_pvo_signal_msft",
        backendurl=variables.get("backend_url"),
    )

    df = yf.download("MSFT", period="234d", progress=False)
    snippet = PercentageVolumeOscillator(df["Volume"], fillna=True).pvo_signal()
    avg = snippet.median()

    portfolio = bot.getPortfolio()

    if snippet[-1] >= avg:
        if portfolio.get("MSFT", 0) == 0:
            # buy msft
            print("buying MSFT")
            bot.buy("MSFT", amount=portfolio.get("USD", 0))
        else:
            print("buy signal, but already holding MSFT")
    else:
        if portfolio.get("MSFT", 0) > 0:
            # sell msft
            print("selling all MSFT")
            bot.sell("MSFT")
        else:
            print("sell signal, but not holding MSFT")
