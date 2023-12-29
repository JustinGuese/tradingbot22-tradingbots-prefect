from getBotData import getBotData
from prefect.client.schemas.schedules import CronSchedule
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    getBotData,
    name="0_ai-investing-website-update",
    schedule=CronSchedule(cron="0 10 * * *"),
)
deployment.apply()
