from os import environ

import yfinance as yf
from basebot22.basebot import BaseBot
from prefect import flow, task, variables
from prefect.filesystems import GitHub
from tradingpatterns.tradingpatterns import detect_head_shoulder

# github_block = GitHub.load("tradingbot-repo")
LOOKBACK = 3


@task
def setup():
    print("connecting to backend...")
    bot = BaseBot(
        "head-and-shoulders-qqq",
        backendurl=variables.get("backend_url"),
    )
    print("get portfolio")
    portfolio = bot.getPortfolio()
    print("downloading QQQ data...")
    df = yf.download("^IXIC", period="1mo", progress=False)
    print("detecting head and shoulder pattern...")
    df = detect_head_shoulder(df)
    return bot, df, portfolio


@task
def get_signal(df):
    for i in range(len(df)):
        signal = df["head_shoulder_pattern"][-i]
        if signal == "Head and Shoulder":
            signal = "buy"
            break
        elif signal == "Inverse Head and Shoulder":
            signal = "sell"
            break
        else:
            signal = None
    print("current head and shoulder signal: %s at lookback %s" % (str(signal), str(i)))
    return signal


@task
def act(signal, bot: BaseBot, portfolio):
    # check if we have money
    usd = portfolio.get("USD", 0)
    if signal == "buy":
        if usd > 10:
            tqqq = portfolio.get("TQQQ", 0)
            sqqq = portfolio.get("SQQQ", 0)
            if sqqq > 0:
                print("selling all SQQQ")
                bot.sell("SQQQ")
                portfolio = bot.getPortfolio()
                usd = portfolio.get("USD", 0)
            if usd > 10:
                print("buying TQQQ with USD: ", usd)
                bot.buy("TQQQ", amount=usd)
                portfolio = bot.getPortfolio()  # refresh
            else:
                print("not enough cash to buy tqqq")
        else:
            print("not enough cash to buy TQQQ or already holding")
    elif signal == "sell":
        # check if we have aapl
        tqqq = portfolio.get("TQQQ", 0)
        sqqq = portfolio.get("SQQQ", 0)
        if tqqq > 0:
            print("selling all TQQQ")
            bot.sell("TQQQ")
            portfolio = bot.getPortfolio()
            usd = portfolio.get("USD", 0)
        if usd > 10:
            print("buying SQQQ with USD: ", usd)
            bot.buy("SQQQ", amount=usd)
            portfolio = bot.getPortfolio()
        else:
            print("not enough cash to buy sqqq")
    else:
        print("no signal in the last %s days" % str(LOOKBACK))


@flow(log_prints=True)
def headAndShoulderFlowGit():
    print("ich starte digga")
    bot, df, portfolio = setup()
    signal = get_signal(df)
    act(signal, bot, portfolio)
    print("portfolio:")
    print(portfolio)


# if __name__ == "__main__":
# headAndShoulderPrefect.deploy(
#     name="head-and-shoulders-qqq",
#     work_pool_name="caprover-prefect-docker-worker",
#     cron="0 9 * * *",
#     image="guestros/tradingbot-prefect-agent:latest",
#     # job_variables={"env": {"EXAMPLE": "boto3"}},
#     push=False,
# )
# deployment = Deployment.build_from_flow(
#     headAndShoulderPrefect, name="head-and-shoulders-qqq"
# )
# deployment.location = ""  # override
# deployment.apply()
