import os
import subprocess
from datetime import datetime

from prefect import flow, task, variables


@task
def runPythonScripts():
    # print current working directory
    print("current working directory: ", os.getcwd())
    subprocess.run(
        ["python", "getBotData.py"],
        capture_output=True,
        cwd="tradingbot-website-generator/src/",
    )


@task
def hugoBuild():
    # delete everything in "public" folder recursively
    try:
        subprocess.run(
            ["rm", "-rf", "public/*"], cwd="tradingbot-website-generator/hugo/"
        )
    except Exception as e:
        print(
            "could not delete contents of public folder, should be alright... " + str(e)
        )

    subprocess.run(
        ["hugo", "--minify", "-d", "public"],
        cwd="tradingbot-website-generator/hugo/",
    )

    with open("tradingbot-website-generator/hugo/public/lastUpdate.txt", "w") as file:
        file.write(str(datetime.utcnow()))


@flow(log_prints=True)
def runAiInvestWebsiteUpdate():
    runPythonScripts()
    hugoBuild()
