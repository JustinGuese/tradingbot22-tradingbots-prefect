# jupyternotebooks/taestimator.ipynb
import pickle
from os import environ

import numpy as np
import pandas as pd
import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables
from ta import add_all_ta_features


@flow(log_prints=True)
def msftDecisionTree():
    bot = BaseBot(
        "msft-decisiontree",
        backendurl=variables.get("backend_url"),
    )

    msft = yf.download("MSFT", period="2mo", progress=False)
    msft = add_all_ta_features(
        msft, open="Open", high="High", low="Low", close="Close", volume="Volume"
    )
    msft = msft.ffill().bfill().fillna(0)

    msft["pct_change"] = msft["Adj Close"].pct_change()
    msft["pct_change_int"] = np.sign(msft["pct_change"]).replace(0, 1).fillna(1)

    with open("msftDecisionTreeModel.pkl", "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(msft)
    portfolio = bot.getPortfolio()
    usd = portfolio.get("USD", 0)
    if predictions[-1] == 1:
        if portfolio.get("MSFT", 0) == 0 and usd > 0:
            bot.buy("MSFT", usd)
            print("Buy all msft")
    else:
        if portfolio.get("MSFT", 0) > 0:
            bot.sell("MSFT", portfolio["MSFT"])
            print("Sell all msft")
