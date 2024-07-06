import re
from glob import glob

base = """- name: brieftech_%s
  version: null
  tags: []
  description: null
  entrypoint: %s:%s
  parameters: {}
  work_pool:
    name: docker-tradingbot-worker
    work_queue_name: docker-tradingbot-worker
    job_variables:
      image: '{{ build-image.image }}'
  schedules:
  - cron: %s
    timezone: UTC
    day_or: true
    active: true"""

full = ""

files = glob("flows/*.py")
for file in files:
    with open(file, "r") as f:
        data = f.read()
    # filter out the value of CRON = "15 18 * * *"
    cron = re.search(r'CRON = "(.*)"', data)
    if cron is not None and len(cron[0]) > 0:
        cron = cron.group(1)
        name = file.split("/")[-1].replace(".py", "")
        full += base % (name, file, "mainFlow", cron) + "\n\n"

with open("prefect.yaml", "a") as f:
    f.write(full)
