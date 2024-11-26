#!/bin/sh

set -e

docker-compose run app sh -c "/scripts/wait-for-it.sh db:5432 && pytest && flake8"