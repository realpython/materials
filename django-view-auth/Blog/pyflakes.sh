#!/bin/bash

echo "============================================================"
echo "== pyflakes =="
pyflakes core | grep -v migration
