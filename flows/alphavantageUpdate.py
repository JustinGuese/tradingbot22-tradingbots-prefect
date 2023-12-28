from os import environ

import requests
from prefect import flow, task, variables


@flow(log_prints=True)
def alphavantageUpdateFlow():
    resp = requests.get(variables.get("backend_url") + "/update/alphavantage/")
    if resp.status_code != 200:
        raise ValueError("Could not update data: ", resp.text)
