# introduction

my tradingbot ideas, basically being published at https://ai-investing-bots.com

## deployment & ci/cd

- flows are executed using the prefect scheduler
- flows are added to prefect cloud using github actions and the prefectAddDeployment.sh script
- flows contain the cron execution time at the top of the file for easier deployment
- the agent will later pull the flow storage from github

- the dockerfile contains everything to run a prefect docker agent in docker
- the ci/cd of the docker agent is handled by my caprover instance, it needs access to the docker socket in order to spawn new containers /var/run/docker.sock:/var/run/docker.sock