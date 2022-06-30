#!/bin/bash


docker run -d -h local --platform linux/amd64 -p 8001:8001 --env-file .env line-provider:latest