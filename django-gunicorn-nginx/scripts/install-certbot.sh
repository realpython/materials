#!/bin/bash

set -eux

if [ $EUID -ne 0 ]; then
  echo "Error: Must be run as root"
  exit 1
fi

apt-get update -y
apt-get install -y software-properties-common
add-apt-repository universe
add-apt-repository ppa:certbot/certbot
apt-get update -y
apt-get install -y certbot python3-certbot-nginx
