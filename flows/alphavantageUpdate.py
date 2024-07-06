from os import environ

import requests
from prefect import flow, task, variables
from prefect.deployments import DeploymentImage


@flow(log_prints=True)
def mainFlow():
    resp = requests.get(variables.get("backend_url") + "/update/alphavantage/")
    if resp.status_code != 200:
        raise ValueError("Could not update data: ", resp.text)


if __name__ == "__main__":
    mainFlow.deploy(
        name="alphavantageUpdate",
        work_pool_name="luxvpsdocker",
        schedule="0 18 * * *",
        image="tradingbot22:latest",
    )
