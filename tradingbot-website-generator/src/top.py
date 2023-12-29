from datetime import datetime

import pandas as pd
from prefect import flow, task, variables

CONTENTPATH = "../hugo/content/english/"


with open("topTemplate.md", "r") as file:
    topTemplate = file.read()

TABLECLASSES = ""  # "table-hover table-dark"


def linkify(botname: str):
    if " " in botname:
        botname = botname.replace(" ", "-")
    botname = botname.lower()
    return f"<a target='_blank' href='/blog/{botname}'>{botname}</a>"


@task
def createTopHugo(summaryDf: pd.DataFrame):
    #   return               sharpe         riskFreeRate
    # static-composer-hedgefundies-excellent-v1  414.52                 6.16                  0.0
    # composer-boring-v1                            0.0  not enough data yet                  0.0
    # composer-bigtechmomentum-v1               -156.81                -2.64                  0.0
    # composer-oppy-opus-v1                      -84.89                -4.67                  0.0

    # topRevenueTable

    # drop all that have 0 revenue
    summaryDf = summaryDf[summaryDf["return % per year"] != 0]

    summaryDf = summaryDf.reset_index()
    summaryDf.rename(columns={"index": "strategy"}, inplace=True)
    summaryDf["strategy"] = summaryDf["strategy"].apply(linkify)

    summaryDf = summaryDf.sort_values(by="return % per year", ascending=False)
    temp = topTemplate.replace(
        "{{topRevenueTable}}",
        summaryDf.to_html(
            index=False,
            table_id="topRevenueTable",
            classes=TABLECLASSES,
            escape=False,
        ),
    )

    # topSharpeTable
    summaryDf = summaryDf.sort_values(by="sharpe ratio", ascending=False)
    temp = temp.replace(
        "{{topSharpeTable}}",
        summaryDf.to_html(
            index=False,
            table_id="topSharpeTable",
            classes=TABLECLASSES,
            escape=False,
        ),
    )

    # topLowRiskTable
    summaryDf = summaryDf.sort_values(by="risk free rate", ascending=False)
    temp = temp.replace(
        "{{topLowRiskTable}}",
        summaryDf.to_html(
            index=False,
            table_id="topLowRiskTable",
            classes=TABLECLASSES,
            escape=False,
        ),
    )

    # finally save
    with open(CONTENTPATH + "top.md", "w") as file:
        file.write(temp)
