import subprocess
from datetime import datetime

import pandas as pd

IMGPATH = "../hugo/assets/images/plots/"
BLOGPATH = "../hugo/content/english/blog/"


with open("blogTemplate.md", "r") as file:
    blogTemplate = file.read()


def createHugoPost(
    botname: str,
    portfolioWorths: pd.DataFrame,
    description: str,
    metrics: dict,
    qsmetrics: pd.Series,
    trades: pd.DataFrame,
    portfolio: pd.DataFrame,
):
    temp = blogTemplate.replace("{{crntDate}}", datetime.utcnow().strftime("%Y-%m-%d"))
    temp = temp.replace("{{title}}", botname)  # TODO: nice title
    temp = temp.replace("{{titleSlag}}", botname)
    temp = temp.replace("{{description}}", description)

    # preapre worth table
    worthTable = portfolioWorths.to_html(index=False, table_id="portfolioworth")
    temp = temp.replace("{{worthTable}}", worthTable)

    # qs metrics
    qsmetrics = pd.DataFrame(qsmetrics).to_html(index=True, table_id="qsmetrics")
    temp = temp.replace("{{qsmetricsTable}}", qsmetrics)

    # metrics
    for key, value in metrics.items():
        temp = temp.replace("{{" + key + "}}", str(value))

    # trades
    trades = trades.to_html(index=False, table_id="trades")
    temp = temp.replace("{{tradesTable}}", trades)

    # portfolio
    portfolio = portfolio.to_html(index=False, table_id="portfolio")
    temp = temp.replace("{{portfolioTable}}", portfolio)

    # finally save
    with open(BLOGPATH + botname + ".md", "w") as file:
        file.write(temp)


# def hugoBuild():
#     # execute the command "hugo --minify -d public" in the folder "../hugo"
#     subprocess.run(["hugo", "--minify", "-d", "public"], cwd="../hugo")
#     # check result
#     result = subprocess.run(["ls", "public"], cwd="../hugo")
#     if result.returncode != 0:
#         raise Exception("hugo build failed")
#     print("hugo build successful")
