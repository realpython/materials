#!/usr/bin/env python3
import threading

l = threading.RLock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")
