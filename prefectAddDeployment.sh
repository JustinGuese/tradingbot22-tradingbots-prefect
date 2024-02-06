#!/bin/bash
# get all .py files in "flows" folder
ALLFILES=$(find ./flows -name "*.py")
for file in $ALLFILES; do
    filename=$(basename "$file")
    filename="${filename%.*}" 
    # the file has CRON = "0 18 * * *" in the first line, extract the cron expression from it
    cron=$(head -n 1 "$file" | grep -o '".*"' | sed 's/"//g')
    prefect deployment build "$file:mainFlow" -n $filename -q docker-caprover-container-sb -sb  gitlab-repository/tradingbot22-tradingbots-prefect -p docker-caprover-container-sb --cron "$cron"
    # removed docker infra as we are already running in a container -ib docker-container/docker-container-execution
    prefect deployment apply "mainFlow-deployment.yaml"
    # remove the deployment file
    rm "mainFlow-deployment.yaml"
done
