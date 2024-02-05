#!/bin/bash
docker buildx build --platform linux/amd64 -t registry.k8s.datafortress.cloud/tradingbot22-tradingbots-prefect:latest  --push .