#!/usr/bin/env python3
import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")


if __name__ == "__main__":
    threads = list()
    for index in range(3):
        print(f"Main    : create and start thread {index}.")
        x = threading.Thread(target=thread_function, args=[index,])
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print(f"Main    : before joining thread - This is where we wait for thread {index}.")
        thread.join()
        print(f"Main    : thread {index} done")

'''
$ ./single_thread.py
Thread 0 starting
Thread 1 starting
Thread 2 starting
before joining thread - This is where we wait for the thread.
Thread 1 finishing
Thread 0 finishing
all done
before joining thread - This is where we wait for the thread.
Thread 2 finishing
all done
before joining thread - This is where we wait for the thread.
all done
'''
