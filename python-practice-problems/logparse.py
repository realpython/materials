#!/usr/bin/env python3
""" log parser
    Accepts a filename on the command line.  The file is a linux-like log file
    from a system you are debugging.  Mixed in among the various statements are
    messages indicating the state of the device.  They look like:
        Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
    The device state message has many possible values, but this program only
    cares about three: ON, OFF, and ERR.

    Your program will parse the given log file and print out a report giving
    how long the device was ON, and the time stamp of any ERR conditions.
"""


if __name__ == "__main__":
    # TODO: Your code goes here
    print("There are no unit tests for logparse.")
