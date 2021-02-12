#!/bin/bash

./gen_certs.sh

DOCKER_BUILDKIT=1 docker build . -f marketplace/Dockerfile -t marketplace --secret id=ca.key,src=ca.key
DOCKER_BUILDKIT=1 docker build . -f recommendations/Dockerfile -t recommendations --secret id=ca.key,src=ca.key

docker-compose up
