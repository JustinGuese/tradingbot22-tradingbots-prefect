import os
import subprocess
from datetime import datetime

from prefect import flow, task, variables

# must be absolute, because prefect uses tmpdirs
HUGO_WORKDIR = "/app/flows/tradingbot-website-generator"


@task
def runPythonScripts():
    global HUGO_WORKDIR
    # print current working directory
    print("current working directory: ", os.getcwd())
    subprocess.run(
        ["python", "getBotData.py"],
        capture_output=True,
        cwd=HUGO_WORKDIR + "/src/",
    )


@task
def hugoBuild():
    global HUGO_WORKDIR
    # delete everything in "public" folder recursively
    try:
        subprocess.run(["rm", "-rf", "public/*"], cwd=HUGO_WORKDIR + "/hugo/")
    except Exception as e:
        print(
            "could not delete contents of public folder, should be alright... " + str(e)
        )

    subprocess.run(
        ["hugo", "--minify", "-d", "public"],
        cwd=HUGO_WORKDIR + "/hugo/",
    )

    with open(HUGO_WORKDIR + "/hugo/public/lastUpdate.txt", "w") as file:
        file.write(str(datetime.utcnow()))


@flow(log_prints=True)
def runAiInvestWebsiteUpdate():
    runPythonScripts()
    hugoBuild()
