#!/bin/bash

echo "============================================================"
echo "== pyflakes =="
pyflakes `./manage.py print_setting LOCAL_APPS` | grep -v migration
