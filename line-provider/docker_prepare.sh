#!/bin/bash


# docker build -f develop.dockerfile -t line-provider .
# createdb bet
# ./env/bin/alembic upgrade head
cp dev.env .env
echo "Successful prepared docker image"
