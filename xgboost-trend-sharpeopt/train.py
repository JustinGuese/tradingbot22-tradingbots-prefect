import pickle

import pandas as pd
import yfinance as yf
from helpers import labelToSignal
from skfolio.moments import DenoiseCovariance, ShrunkMu
from skfolio.optimization import MeanRisk, ObjectiveFunction
from skfolio.preprocessing import prices_to_returns
from skfolio.prior import EmpiricalPrior
from sklearn.model_selection import train_test_split
from ta import add_all_ta_features
from trendet import identify_df_trends
from xgboost import XGBClassifier

### START: / TICKER SELECTION
data = pd.read_csv("../jupyternotebooks/myvwtcnasdaq.csv")

tickers = data["Ticker"].tolist()
# kick out nan
tickers = [x for x in tickers if isinstance(x, str)]
del data
# df = yf.download(
#     tickers,
#     period="1y",
# )
# df.to_parquet("myvwtcnasdaq.parquet")
print("loading data from parquet")
df = pd.read_parquet("myvwtcnasdaq.parquet")
fullDf = df.swaplevel(axis=1)
df = df["Adj Close"]
# kick out columns which are all nan
df = df.dropna(axis=1, how="all")

X = prices_to_returns(df)

model = MeanRisk(
    objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
    prior_estimator=EmpiricalPrior(
        mu_estimator=ShrunkMu(), covariance_estimator=DenoiseCovariance()
    ),
)

model.fit(X)

portfolio = model.predict(X)

# print(portfolio.annualized_sharpe_ratio)
# print(portfolio.summary())

invest = pd.DataFrame(model.weights_, columns=["weight"])
invest["ticker"] = df.columns
invest = invest.set_index("ticker")
invest = invest.sort_values(by="weight", ascending=False)
invest = invest[invest["weight"] > 0]
# print(invest["weight"].sum())

toInvest = invest.head(10)
print("current ticker selection: ", toInvest)
### END: DATA PREPARATION / TICKER SELECTION

### START: DATA PREP
for ticker in list(toInvest.index):
    df = fullDf[ticker]
    df = add_all_ta_features(
        df, open="Open", high="High", low="Low", close="Close", volume="Volume"
    )
    df = identify_df_trends(df, "Close")
    df["Signal"] = labelToSignal(df)

    Y = (
        df["Signal"].shift(-7).ffill().bfill()
    )  # shift signal by 1 week to predict future
    X = df.drop(["Up Trend", "Down Trend"], axis=1)  # bc signal has that info
    del df
    Y = Y.replace(-1, 0)
    X, _, Y, _ = train_test_split(X, Y, test_size=0.001, shuffle=True)

    model = XGBClassifier()
    model.fit(X, Y)
    print("xgb model score for " + ticker + " " + str(model.score(X, Y)))
    # save model
    pickle.dump(model, open(ticker + ".model", "wb"))
### END: DATA PREP
toInvest.to_csv("toInvest.csv")
print("done")
