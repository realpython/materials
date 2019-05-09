"""
This module contains a simple class to measure elapsed time
"""

import time


class ET(object):
    def __init__(self):
        self.start_time = time.time()

    def __call__(self):
        return time.time() - self.start_time
