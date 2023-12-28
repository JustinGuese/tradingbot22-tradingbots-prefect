#!/bin/bash
python addAllFlows.py
prefect worker start --pool caprover-docker-container