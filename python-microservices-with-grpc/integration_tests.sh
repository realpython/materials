#!/bin/bash

set -euo pipefail

docker-compose up -d
trap "docker-compose down" EXIT

sleep 5  # Give the services time to warm up
docker-compose exec marketplace pytest
