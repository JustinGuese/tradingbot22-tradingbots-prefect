import base64
from io import BytesIO

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from hugofy import IMGPATH, createHugoPost
from quantstats.reports import metrics as qs_metrics
from top import createTopHugo

matplotlib.use("Agg")
from db import Bot, PortfolioWorths, SessionLocal, Trade


def worthStringify(worthfloat):
    return str(worthfloat) + "€"


def plt2Base64(fig):
    # Save the plot as a BytesIO object
    buffer = BytesIO()
    canvas = fig.canvas
    canvas.print_png(buffer)
    buffer.seek(0)

    # Convert the BytesIO object to a base64 string
    plot_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    return plot_base64


def getBotDescription(botname: str, allBots: list):
    descr = None
    for bot in allBots:
        if bot.name == botname:
            descr = bot.description
            break
    return descr


PRICESTORE = dict()


def getPrice(ticker: str) -> float:
    if ticker == "USD":
        return 1
    if ticker in PRICESTORE:
        return PRICESTORE[ticker]
    else:
        try:
            price = round(yf.Ticker(ticker).history(period="1d")["Close"].iloc[0], 2)
        except:
            price = 0
        PRICESTORE[ticker] = price
        return price


def getBotData():
    db = SessionLocal()
    allBots = db.query(Bot).all()
    # for each bot get the portfolioworths
    allBotNames = [bot.name for bot in allBots]

    allBotStats = dict()
    for botname in allBotNames:
        nicename = allBots[allBotNames.index(botname)].nicename

        portfolioWorths = (
            db.query(PortfolioWorths.timestamp, PortfolioWorths.worth)
            .filter(PortfolioWorths.bot == botname)
            .order_by(PortfolioWorths.timestamp.desc())
            .all()
        )
        df = pd.DataFrame(portfolioWorths, columns=["Date", "Portfolio Worth"])
        if len(df) == 0:
            print("no data for bot", botname)
            continue
        # set date to midnight
        df["Date"] = pd.to_datetime(df["Date"]).dt.date

        # startmoney
        startMoney = (
            10000
            if df["Portfolio Worth"].iloc[-1] > 10000
            else df["Portfolio Worth"].iloc[-1]
        )

        # create plot
        color = "g" if df["Portfolio Worth"].iloc[0] >= startMoney else "r"

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df["Date"], df["Portfolio Worth"], color=color)
        ax.set_xlabel("Date")
        ax.set_ylabel("Portfolio Worth in EUR")
        ax.set_title(nicename)
        ax.tick_params(axis="x", rotation=45)
        plt.tight_layout()

        plt.savefig(IMGPATH + nicename if nicename else botname + ".png")
        # b64plot = plt2Base64(fig)
        plt.close(fig)

        # continue with key metrics
        # returnPA, daysActive
        returnNow = df["Portfolio Worth"].iloc[0] - df["Portfolio Worth"].iloc[-1]
        daysActive = (df["Date"].iloc[0] - df["Date"].iloc[-1]).days

        try:
            returnPA = int(
                ((returnNow / daysActive) * 365) / df["Portfolio Worth"].iloc[-1] * 100
            )  # startmoney
        except ValueError:
            returnPA = 0
        crntCapital = df["Portfolio Worth"].iloc[0]

        metrics = {
            "returnPA": returnPA,
            "daysActive": daysActive,
            "crntCapital": crntCapital,
            "startMoney": startMoney,
        }

        # continue with advanced metrics
        onlyReturns = df
        onlyReturns["Date"] = pd.to_datetime(onlyReturns["Date"])
        onlyReturns = onlyReturns.set_index("Date")[::-1][
            "Portfolio Worth"
        ].pct_change()
        # convert to series
        onlyReturns = pd.Series(onlyReturns)

        try:
            qsmetrics = qs_metrics(onlyReturns, display=False)
        except Exception:
            qsmetrics = pd.Series(["not enough data yet"])

        try:
            sharpe = str(float(qsmetrics.T["Sharpe"].iloc[0]))
        except:
            sharpe = "not enough data yet"
        try:
            riskFreeRate = str(float(qsmetrics.T["Risk-Free Rate"].iloc[0]))
        except:
            riskFreeRate = "not enough data yet"

        allBotStats[nicename if nicename else botname] = {
            "return % per year": returnPA,
            "sharpe ratio": sharpe,
            "risk free rate": riskFreeRate,
        }

        # make nice readable
        # date conversion is done in datatable
        # df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d.%m.%Y")
        df["Portfolio Worth"] = df["Portfolio Worth"].apply(worthStringify)

        ## last trades
        trades = (
            db.query(
                Trade.timestamp, Trade.buy, Trade.ticker, Trade.price, Trade.quantity
            )
            .filter(Trade.bot == botname)
            .order_by(Trade.timestamp.desc())
            .limit(5)
            .all()
        )
        trades = pd.DataFrame(
            trades, columns=["Date", "Buy/Sell", "Ticker", "Price", "Qty"]
        )
        trades["Volume"] = round(trades["Price"] * trades["Qty"], 2)
        trades["Buy/Sell"] = trades["Buy/Sell"].apply(lambda x: "Buy" if x else "Sell")

        # portfolioTable
        portfolio = allBots[allBotNames.index(botname)].portfolio
        portfolio = pd.DataFrame(portfolio.items(), columns=["Ticker", "Qty"])
        portfolio["Crnt Price"] = portfolio["Ticker"].apply(getPrice)
        portfolio["Worth (USD)"] = round(portfolio["Crnt Price"] * portfolio["Qty"], 2)
        portfolio = portfolio.sort_values(by="Worth (USD)", ascending=False)

        createHugoPost(
            botname,
            nicename,
            df,
            getBotDescription(botname, allBots),
            metrics,
            qsmetrics,
            trades,
            portfolio,
        )
    # then finally create the summary
    allBotStats = pd.DataFrame(allBotStats).T
    createTopHugo(allBotStats)


if __name__ == "__main__":
    getBotData()
