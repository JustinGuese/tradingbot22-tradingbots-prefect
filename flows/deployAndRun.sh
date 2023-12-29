#!/bin/bash
python addAllFlows.py
# little detour to add ai investing bots task as well
cd ../tradingbot-website-generator/src/
python addFlowToPrefect.py
cd ../../flows
prefect worker start --pool caprover-docker-container