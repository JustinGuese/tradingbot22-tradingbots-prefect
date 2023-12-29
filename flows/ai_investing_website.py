import subprocess

from prefect import flow, task, variables


@task
def runPythonScripts():
    result = subprocess.run(
        ["python", "getBotData.py"],
        capture_output=True,
        cwd="tradingbot-website-generator/src/",
    )
    if result.returncode != 0:
        print(result.stderr.decode("utf-8"))
        raise Exception("getBotData.py failed")
    print(result.stdout.decode("utf-8"))


@task
def hugoBuild():
    result = subprocess.run(
        ["hugo", "--minify", "-d", "public"], cwd="tradingbot-website-generator/hugo/"
    )
    if result.returncode != 0:
        print(result.stderr.decode("utf-8"))
        raise Exception("hugo build failed")
    print(result.stdout.decode("utf-8"))


@flow(log_prints=True)
def runAiInvestWebsiteUpdate():
    runPythonScripts()
    hugoBuild()
