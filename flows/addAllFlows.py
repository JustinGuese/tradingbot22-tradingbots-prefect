import headShoulderPrefect
from prefect.client.schemas.schedules import CronSchedule
from prefect.deployments import Deployment
from tqdm import tqdm

# all flows
FLOWS = [
    (headShoulderPrefect.headAndShoulderFlow, "head-and-shoulders-qqq", "0 9 * * *"),
]

for flow, name, cron in tqdm(FLOWS):
    print("building flow: ", name)
    deployment = Deployment.build_from_flow(
        flow, name=name, schedule=CronSchedule(cron=cron)
    )
    deployment.apply()
