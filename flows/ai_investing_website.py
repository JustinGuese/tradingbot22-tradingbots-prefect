import os
import subprocess

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
    subprocess.run(
        ["hugo", "--minify", "-d", "public"],
        cwd="tradingbot-website-generator/hugo/",
    )


@flow(log_prints=True)
def runAiInvestWebsiteUpdate():
    runPythonScripts()
    hugoBuild()
