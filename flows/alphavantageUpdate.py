CRON = "0 18 * * *"  # this doesnt do anything in the script, but is used by the prefect deployment script
from os import environ

import requests
from prefect import flow, task, variables


@flow(log_prints=True)
def mainFlow():
    resp = requests.get(variables.get("backend_url") + "/update/alphavantage/")
    if resp.status_code != 200:
        raise ValueError("Could not update data: ", resp.text)
