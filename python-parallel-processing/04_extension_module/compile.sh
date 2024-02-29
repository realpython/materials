#!/bin/bash

gcc $(python3-config --cflags) -shared -fPIC -O3 -o fibmodule.so fibmodule.c

